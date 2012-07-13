#!/usr/bin/env python
# coding=utf-8

import urlparse
from bs4 import BeautifulSoup, Comment
from mechanize import Browser
from AppInfo import AppInfo

class DcnApp:
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
		urls = soup.find_all("a", attrs={"class" : "gamesoft_link"})
		
		return [ parts._replace(path=url.get('href')).geturl() for url in urls ]

	def get_app_pages(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "pager"})
		urls = snippet.find_all("a")
		
		parts = urlparse.urlparse(uri)
		return list(set([uri] + [ parts._replace(path=url.get('href')).geturl() for url in urls ]))

	def get_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")

		info = AppInfo()
		div_viewbox = soup.find('div', attrs={"class" : "info_title"})
		info.name = div_viewbox.text
		info.category = ""
		info.version = ""
		info.size = ""
		info.updated = ""
		info.price = ""
		info.os = ""
		info.developer = ""
		info.language = ""
		desc = soup.find('div', attrs={"class" : "rom_introductioncon yingyong_intro"}).text
		info.description = desc

		artwork = soup.find('div', attrs={"class" : "yingyong_img"}).img["src"]
		info.artwork = self.br.retrieve(artwork)[0]
		
		div_images = soup.find('div', attrs={"class" : "snapshot_list"})
		images = div_images.find_all('img')
		info.images = [self.br.retrieve(img["src"])[0] for img in images]

		info.debug()
		return info
	