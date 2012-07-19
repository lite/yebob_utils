#!/usr/bin/env python
# coding=utf-8

import re, urlparse
from bs4 import BeautifulSoup, Comment
from mechanize import Browser
from AppInfo import AppInfo

class WinPhoneApp:
	def __init__(self):
		self.br = Browser()
	
	def get_app_links(self, uri):
		parts = urlparse.urlparse(uri)
		if "/apps/" in parts.path:
			return [uri]

		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('table', attrs={"class" : "apps"})
		urls = snippet.find_all("a")
		
		return list(set([ parts._replace(path=url.get('href'), query="").geturl() for url in urls ]))

	def get_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")

		info = AppInfo()
		div_viewbox = soup.find(id="application")
		info.name = div_viewbox.h1.renderContents()
		info.category = ""
		info.version = ""
		info.size = ""
		info.updated = ""
		info.price = ""
		info.os = "Windows Phone"
		info.developer = ""
		info.language = ""
		desc = soup.find(id="appDetails").pre.prettify()
		info.description = desc

		artwork = soup.find(id="appSummary").img["src"]
		info.artwork = artwork
		
		div_images = soup.find(id="screenshots")
		images = div_images.find_all('a')
		info.images = [img["href"] for img in images]
		
		info.debug()
		return info
	