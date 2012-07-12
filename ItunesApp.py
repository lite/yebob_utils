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
		#info.name = soup.html.head.title.renderContents()
		info.name = soup.find(id="content").h1.renderContents()
		info.category = ""
		info.version = ""
		info.size = ""
		info.updated = ""
		info.price = ""
		info.os = "iOS"
		developer = soup.find(id="desktopContentBlockId").h2.renderContents()
		info.developer = developer[12:-1] 
		info.language = ""
		desc = soup.find('div', attrs={"class" : "product-review"}).p.text
		info.description = desc
		
		artwork = soup.find(id="left-stack").div.img["src"]
		info.artwork = self.br.retrieve(artwork)[0]
		
		div_images = soup.find('div', attrs={"class" : "screenshots"})
		print div_images
		images = div_images.find_all('img')
		info.images = [self.br.retrieve(img["src"])[0] for img in images]

		info.debug()
		return info
