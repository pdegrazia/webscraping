'''
@author paolo
main module to start using requests and lxml to scrape web pages
'''

import requests

resp = requests.get('http://www.gazzetta.it')
print resp.status_code