#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
from mechanize import Browser
from AppInfo import AppInfo

class ItunesApp:
	def __init__(self):
		self.br = Browser()
		self.br.addheaders = [("HTTP_CONNECTION", "keep-alive")]
		
	def get_app_links(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")
		tags = soup.find(id="selectedcontent")
		urls = tags.findAll('a')
		
		return [ url.get('href') for url in urls ]
			
	def get_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")
		info = AppInfo()
		info.name = soup.find(id="title").h1.renderContents()
		info.category = "Education"
		info.version = "2.1"
		info.size = "19.1MB"
		info.updated = "2011-12-30"
		info.price = "Free"
		info.developer = soup.find(id="title").h2.renderContents()
		info.language = "English"
		info.description = soup.find('div', attrs={"class" : "product-review"}).p.renderContents().replace("<br />", "\n")
		
		artwork = soup.find(id="left-stack").div.img["src"]
		info.artwork = self.br.retrieve(artwork)[0]
		
		#info.debug()
		return info
