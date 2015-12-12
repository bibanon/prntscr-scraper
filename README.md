Prntscr.com Scraper
===================

> **Note:** This is not finished yet. The web scraping component hasn't yet been written.

This scraper is designed to grab all Imgur URLs from Prntscr.com. This site is effectively a URL redirector, so it would be a good idea to archive it such that the links don't break when it does.

This scraper utilizes a SQLite database to keep everything together.

## ETA

As of this writing, there are 566574270 images on Prntscr. Here's a rough estimate of scraping time:

* `566574270/60/60/60/24` = 1 second delay, ~100-120 days
* `566574270/60/60/60/24/10` = 100 millisecond delay, ~10-12 days

## Usage

1. The first step is to initialize the SQLite database, `prntscr.db`. If the database already exists, you will need to move or delete the existing one before creating a new one.

        python3 0-create-db.py

2. The next step is to scrape the image urls. If you need to pause and continue later, press Ctrl-C to stop and save changes.

        python3 1-get-urls.py 566574270

3. If you want to start at a certain index, instead of `0`, put in two arguments (start, stop):

        python3 1-get-urls.py 1679616 566574270

3. Once all URLs have been scraped, the results will be in the `prntscr.db` SQLite database.

You can also edit `settings.py` to change delays and other settings.
