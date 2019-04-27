# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Medium_Scrape:
	"""Scrapes a Medium Website"""
	def __init__(self, arg):
		"""
		needs a url link
		"""
		self.url = arg

	def print_url(self):
		"""
		prints the url
		"""
		print(self.url)

	def scrape_site(self):
		page = urlopen(self.url)
		# parse the html using beautiful soup and store in variable `soup`
		soup = BeautifulSoup(page, "html.parser")
		name_box = soup.find("p", attrs={"class": "graf"})
		name = name_box.text.strip() # strip() is used to remove starting and trailing
		print (name)



