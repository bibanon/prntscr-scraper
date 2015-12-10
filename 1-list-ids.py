#!/usr/bin/python3
# prntscr.com Imgur URL scraper
# 1-list-ids.py
# Populate the database with sequential base36 IDs.
# Written by Antonizoon for the Bibliotheca Anonoma Scripting Commission

import sys
import dataset

# custom base36 encoding tools
from base36 import *

# constant filenames
db_fname = "prntscr.db"

# main method
def main():
	if len (sys.argv) != 2 :
		print("prntscr.com Imgur URL scraper")
		print("%s - Populates the database with sequential base36 ids." % (sys.argv[0]))
		print("You must create a database using 0-create-db.py first.")
		print("\tUsage: %s <total_images>" % (sys.argv[0]))
		sys.exit(1)
	
	# tell the program where to stop listing
	stop = int(sys.argv[1])
	
	# access the database with table `images`
	db = dataset.connect('sqlite:///%s' % db_fname)
	
	# determine the latest item added from descending order
	results = db['images'].find_one(order_by=['-id']) 
	
	# if database is not empty, start from last modified
	if (results is not None):
		start = results['id'] + 1
	else:
		start = 0
	print("Starting from ID: %s, Base 36: %s" % (start, tobase36(start)))

	# Conduct as SQL Transaction to reduce commits
	with db as tx:
		for i in range(start, stop + 1):
			# create source URL
			base36_id = tobase36(i)
			source_url = "http://prntscr.com/%s" % base36_id
			
			# download HTML and parse for imgur URL
			img_url = "" # placeholder
			
			# insert into table
			tx['images'].insert(dict(id=i, img_id=base36_id, img_url=img_url))
			
			print("Inserted ID: %s, Base 36: %s, URL: %s" % (id, base36_id, img_url))

	# display the latest additions
	result = db['images'].find(order_by=['-id'], _limit=10)
	for row in result:
		print("%d\t\t%s" % (row['id'], row['img_id']))

if __name__ == "__main__":
	main()