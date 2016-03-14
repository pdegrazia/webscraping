'''
@author paolo
main module to start using requests and lxml to scrape web pages
'''

import requests
from lxml import html


class Scraper:
	def __init__(self, url = None):
		self.resp = None
		self.url = url

	def set_url(self,url):
		self.url = url

	def retrieve_data(self):
		try:
			self.resp = requests.get(self.url)
			if not self.check_status_code(200):
				print 'Wrong status code! Expected: 200, Actual: %s' % self.resp.status_code
		except:
			print 'Could not connect to url %s' % self.url

	def check_status_code(self,expected):
		if self.resp.status_code == expected:
			return True

	def set_search_pattern(self,pattern):
		self.pattern = pattern


	def find_elements(self):
		tree = html.fromstring(self.resp.content)
		links = tree.xpath(self.pattern)
		return links


if __name__ == '__main__':

	scraper = Scraper(url='http://www.repubblica.it')
	scraper.retrieve_data()
	scraper.set_search_pattern('//article/header/h1/a')
	links = scraper.find_elements()

	for link in links:
		if link.text != ' ':
			try:
				print 'Title: %s' % link.text.lstrip()
			except:
				print 'Object is none'