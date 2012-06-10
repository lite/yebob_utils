#!/usr/bin/env python
# coding=utf-8

from bs4 import BeautifulSoup
from mechanize import Browser
from AppInfo import AppInfo
import re

class GooglePlayApp:
	host="https://play.google.com"

	def __init__(self):

		self.br = Browser()
		self.br.addheaders = [("HTTP_CONNECTION", "keep-alive"), 
                     #("HTTP_KEEP_ALIVE", "300"), 
                     #("HTTP_ACCEPT", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
                     #("HTTP_ACCEPT_ENCODING", "gzip,deflate"), 
                     #("HTTP_ACCEPT_LANGUAGE", "en-us,en;q=0.5"), 
                     #("HTTP_USER_AGENT", "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0")
                     ]
		
	def get_app_links(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "num-pagination-page"})
		urls = snippet.find_all("a", attrs={"class" : "title"})
		
		return [ self.host+url.get('href') for url in urls ]
			

	def get_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data)
		info = AppInfo()
		info.name = soup.find('h1', attrs={"class" : "doc-banner-title"}).renderContents()
		info.category = "Education"
		info.version = "2.1"
		info.size = "19.1MB"
		info.updated = "2011-12-30"
		info.price = "Free"
		info.developer = soup.find('a', attrs={"class" : "doc-header-link"}).renderContents()
		info.language = "English"
		# info.description = soup.find('div', attrs={"class" : "product-review"}).p.renderContents().replace("<br />", "\n")
		info.description = soup.find(id="doc-original-text").renderContents()

		artwork = soup.find('div', attrs={"class" : "doc-banner-icon"}).img["src"]
		info.artwork = self.br.retrieve(artwork)[0]
		
		info.debug()
		return info
