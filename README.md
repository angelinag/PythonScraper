# Simple Python web scraper

<a name="run"/>

## How to run
Run the `start.py` file in the root dir.

<a name="desc"/>

## Description
Web scraper that scrapes `https://www.yelp.com/biz/american-airlines-irving` for user reviews and exports the data into an Excel file locally (at `D:\`).

## Approach used for scraping
This webpage in particular uses a lot of dynamically generated classes. I was able to determine a way to grasp onto 3 out of 4 required data fields by finding specific attribute filters, and the last 1 I had to reach by traversing the DOM from a known point.

## Packages used
- `requests` for fetching
- `bs4` and `re` for parsing
- `win32py` for excel export