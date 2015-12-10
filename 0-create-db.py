#!/usr/bin/python3
# prntscr.com Imgur URL scraper
# 0-create-db.py
# Create a dataset database to store Imgur IDs
# Written by Antonizoon for the Bibliotheca Anonoma Scripting Commission
import dataset

# filenames
db_fname = "prntscr.db"

# create a database with table `images` and primary
db = dataset.connect('sqlite:///%s' % db_fname)
db.query('CREATE TABLE images (id INT PRIMARY KEY NOT NULL, img_id VARCHAR(6), img_url TEXT); ')