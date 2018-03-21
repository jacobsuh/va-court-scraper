# VA Circuit Court Case Database Scraper
Automatically scrapes [Virginia's circuit court case databases](http://ewsocis1.courts.state.va.us/CJISWeb/circuit.jsp) with supplied dates and pulls relevant data. Created for a UVa student's Global Security and Justice thesis paper.

*court_scraper.py* scrapes cases from randomly generated dates, supplied by *get_dates.py*.

*name_scraper.py* parses the names from the *court_scraper.py* output and searches for any other cases with the same defendant in every other county.

Utilizes Selenium and BeautifulSoup. Main challenge was that the database utilizes javascript almost entirely, so regular GET/POST requests couldn't be used. Selenium was used to physically click on elements and enter in keys as needed. The HTML source was then passed to BeautifulSoup to scrape the necessary data points for the paper.

Date generator created by [Steven Stetzler](https://github.com/stevenstetzler).