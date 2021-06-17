# Price checker

It checks prices on websites which you define and when the price change, it will send an email to you and open a notepad to notify you.

## Technical details
It's using BeautifulSoup to pull text from websites. 
Then it's using python interface called ezgmail for sending email via Gmail API which you first should enable on:
https://developers.google.com/gmail/api/quickstart/python/
Then download credentials.json and lastly after issuing command ezgmail.init() download token.json. These files should be in the same folder as your python script.
Ezgmail is easy to use and more info is here: https://pypi.org/project/EZGmail/

