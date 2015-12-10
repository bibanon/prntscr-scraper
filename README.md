Prntscr.com Scraper
===================

> **Note:** This is not finished yet. The web scraping component hasn't yet been written.

This scraper is designed to grab all Imgur URLs from Prntscr.com. This site is effectively a URL redirector, so it would be a good idea to archive it such that the links don't break when it does.

This scraper utilizes a SQLite database to keep everything together.

## Usage

1. The first step is to initialize the database.
        python3 0-create-db.py
2. The next step is to scrape the data.
        python3 1-list-ids.py 564956820