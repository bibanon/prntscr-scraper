#!/usr/bin/python3
# prntscr.com Imgur URL scraper
# settings.py
# Define constants for the program to use.
# Written by Antonizoon for the Bibliotheca Anonoma Scripting Commission

# default database name
db_fname = "prntscr.db"

# HTTP headers for the script to send
headers = {
    'User-Agent': 'Bibliotheca Anonoma Prntscr Archiver v0.0.1'
}

# delay, in seconds
delay = 0.150 # 150ms

# pause if 404 or rate limit
pause = 1 # 1s