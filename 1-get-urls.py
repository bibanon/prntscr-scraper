#!/usr/bin/python3
# prntscr.com Imgur URL scraper
# 1-get-urls.py
# Grab the urls for every image and put it in the database.
# Written by Antonizoon for the Bibliotheca Anonoma Scripting Commission

import sys
import re
import time
import dataset

# web scraping utilities
import requests
from bs4 import BeautifulSoup

# Constants
import settings as s

# custom base36 encoding tools
import base36 as b36

# main method
def main():
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print("prntscr.com Imgur URL scraper")
		print("%s - Grab the urls for every image and put it in the database." % (sys.argv[0]))
		print("You must create a database using 0-create-db.py first.")
		print("\tUsage: %s <stop>" % (sys.argv[0]))
		print("\tUsage: %s <start> <stop>" % (sys.argv[0]))
		sys.exit(1)
	
	# access the database with table `images`
	db = dataset.connect('sqlite:///%s' % s.db_fname)
	
	# one argument (stop)
	if len(sys.argv) == 2:
		# determine the latest item added from descending order
		results = db['images'].find_one(order_by=['-id']) 
		
		# if database is not empty, start from last modified
		if (results is not None):
			start = results['id'] + 1
		else:
			start = 0
		
		# tell the program where to stop
		stop = int(sys.argv[1])
	
	# two arguments (start, stop)
	if len(sys.argv) == 3:
		# tell the program where to start
		start = int(sys.argv[1])
		
		# tell the program where to stop
		stop = int(sys.argv[2])

	print("Starting from ID: %s, Base 36: %s" % (start, b36.tobase36(start)))
	
	# begin a requests session to save performance
	with requests.Session() as session:
		# Conduct as SQL Transaction to reduce commits
		with db as tx:
			try:
				i = start
				while i < stop + 1:
					# create source URL
					base36_id = b36.tobase36(i)
					# insert into table
					source_url = "http://prntscr.com/%s" % base36_id

					# grab HTML
					r = session.get(source_url, headers=s.headers)
					soup = BeautifulSoup(r.text)

					# download HTML and parse for imgur URL
					meta = soup.find(attrs={'name':'twitter:image:src'})
					if (r.status_code == requests.codes.ok and meta != None):
						img_url = meta.get('content')
						# don't store if "image removed" photo provided
						if (re.search("8tdUI8N", img_url) != None):
							img_url = ""
						success = True
					else:
						print(":: Notice: 404 or rate limit. Waiting before continuing...")
						success = False

					if success:		# insert URL if successful
						# insert into table
						tx['images'].insert(dict(id=i, img_id=base36_id, img_url=img_url))
						
						print("Inserted ID: %s, Base 36: %s, URL: %s" % (str(id), base36_id, img_url))
					
						# go to next iteration
						i += 1
						
						# delay before next iteration
						time.sleep(s.delay)
					else:			# wait a while before continuing
						time.sleep(s.pause)
			except KeyboardInterrupt: # commit upon Ctrl-C and stop loop
				print(":: Caught Ctrl-C, stopping...")
				print(":: Committing the transaction...")
				tx.commit()
			except: # also commit upon unexpected errors
				print("Unexpected error:", sys.exc_info()[0])
				tx.commit()
				raise

	# display the latest additions
	result = db['images'].find(order_by=['-id'], _limit=10)
	print(":: Last 10 additions to the database in descending order: ")
	for row in result:
		print("%d\t\t%s\t\t%s" % (row['id'], row['img_id'], row['img_url']))

if __name__ == "__main__":
	main()