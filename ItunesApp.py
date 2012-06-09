#!/usr/bin/env python
# coding=utf-8

from BeautifulSoup import BeautifulSoup
from mechanize import Browser
from AppInfo import AppInfo

class ItunesApp:
	def __init__(self):
		self.br = Browser()
		
	def get_app_links(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data)

		tags = soup.find('div', attrs={"id" : "selectedcontent"}).ul
		urls = tags.findAll('a')
		
		return [ url["href"] for url in urls ]
			

	def get_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data)
		info = AppInfo()
		info.name = soup.find('div', attrs={"id" : "title"}).h1.renderContents()
		info.category = "Education"
		info.version = "2.1"
		info.size = "19.1MB"
		info.updated = "2011-12-30"
		info.price = "Free"
		info.developer = soup.find('div', attrs={"id" : "title"}).h2.renderContents()
		info.language = "English"
		info.description = soup.find('div', attrs={"class" : "product-review"}).p.renderContents().replace("<br />", "\n")
		
		artwork = soup.find('div', attrs={"id" : "left-stack"}).div.img["src"]
		info.artwork = self.br.retrieve(artwork)[0]
		
		#info.debug()
		return info
