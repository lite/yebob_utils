#!/usr/bin/env python
# coding=utf-8

import re
from bs4 import BeautifulSoup, Comment
from mechanize import Browser
from AppInfo import AppInfo

class Www51ipaApp:
	host="http://www.51ipa.com"

	def __init__(self):

		self.br = Browser()
		self.br.addheaders = [("HTTP_CONNECTION", "keep-alive"),]
		self.pat = re.compile('<!--.+-->', re.DOTALL | re.MULTILINE )

	def get_app_pages(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "dede_pages"})
		urls = snippet.find_all("a")
		
		return list(set([uri] + [ uri+url.get('href') for url in urls ]))
		
	def get_app_links(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "listbox"})
		urls = snippet.find_all("a", attrs={"class" : "title"})
		
		return [ self.host+url.get('href') for url in urls ]

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
		desc = soup.find('div', attrs={"class" : "content"}).text
		info.description = self.pat.sub("", desc)

		artwork = soup.find('div', attrs={"class" : "picview"}).img["src"]
		info.artwork = self.br.retrieve(artwork)[0]
		
		info.debug()
		return info
	