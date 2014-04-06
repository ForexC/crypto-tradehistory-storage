crypto-tradehistory-storage
===========================

Python code to store trade history from cryptocurrency broker APIs. Currently supports Cryptsy. Run via Cron.

Example crontab entry for 15 minutes frequency:

0,14,29,44 * * * * cd /home/tradehistory/crypto-tradehistory-storage && python cron.py


Dependencies: 

-- SQLite3 package ('sqlite3' on Ubuntu)
-- Cryptsy API library v0.2 (or better)
https://pypi.python.org/pypi/Cryptsy

Cryptsy.php should be in same directory as cron.py and scrape.py.

Please visit #cryptoforex in Freenode for support or questions.
