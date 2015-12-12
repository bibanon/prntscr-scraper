#!/usr/bin/python3
# prntscr.com Imgur URL scraper
# 0-create-db.py
# Create a dataset database to store Imgur IDs
# Written by Antonizoon for the Bibliotheca Anonoma Scripting Commission
import sys
import dataset
import sqlite3
import settings as s

try:
	# create a database with table `images` and primary
	db = dataset.connect('sqlite:///%s' % s.db_fname)
	db.query('CREATE TABLE images (id INT PRIMARY KEY NOT NULL, img_id VARCHAR(6), img_url TEXT); ')
except:
	print("You need to move or delete the existing database: `%s` before creating a new one." % s.db_fname)
	sys.exit(1)