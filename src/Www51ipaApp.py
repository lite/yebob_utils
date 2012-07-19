#!/usr/bin/env python
# coding=utf-8

import urlparse
from bs4 import BeautifulSoup, Comment
from mechanize import Browser
from AppInfo import AppInfo

class Www51ipaApp:
	def __init__(self):
		self.br = Browser()
		self.br.addheaders = [("HTTP_CONNECTION", "keep-alive"),]
	
	def get_app_links(self, uri):
		parts = urlparse.urlparse(uri)
		if ".html" in parts.path:
			return [uri]

		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "listbox"})
		urls = snippet.find_all("a", attrs={"class" : "title"})
		
		return list(set([ parts._replace(path=url.get('href')).geturl() for url in urls ]))

	def get_app_pages(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "dede_pages"})
		urls = snippet.find_all("a")
		
		parts = urlparse.urlparse(uri)
		return list(set([uri] + [ parts._replace(path=url.get('href')).geturl() for url in urls ]))

	def get_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")

		info = AppInfo()
		div_viewbox = soup.find('div', attrs={"class" : "viewbox"})
		info.name = div_viewbox.h2.renderContents()
		info.category = ""
		info.version = ""
		info.size = ""
		info.updated = ""
		info.price = ""
		info.os = "iOS"
		info.developer = ""
		info.language = ""
		desc = soup.find('div', attrs={"class" : "content"}).prettify()
		info.description = desc

		artwork = soup.find('div', attrs={"class" : "picview"}).img["src"]
		info.artwork = artwork
	
		div_images = soup.find('div', attrs={"class" : "content"})
		images = div_images.find_all('img')
		info.images = [img["src"] for img in images]
	
		info.debug()
		return info
	