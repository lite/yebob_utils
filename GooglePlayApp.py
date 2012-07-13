#!/usr/bin/env python
# coding=utf-8

import urlparse
from bs4 import BeautifulSoup
from mechanize import Browser, CookieJar
from AppInfo import AppInfo

class GooglePlayApp:
	def __init__(self):
		self.br = Browser()
		self.cj = CookieJar()
		self.br.set_cookiejar(self.cj)
		self.br.addheaders = [("HTTP_CONNECTION", "keep-alive"), 
                     ("HTTP_KEEP_ALIVE", "300"), 
                     ("HTTP_ACCEPT", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
                     ("HTTP_ACCEPT_ENCODING", "gzip,deflate"), 
                     ("HTTP_ACCEPT_LANGUAGE", "en-us,en;q=0.5"), 
                     ("HTTP_USER_AGENT", "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20100101 Firefox/12.0")
                     ]
		
	def get_app_links(self, uri):
		parts = urlparse.urlparse(uri)
		if "/store/apps/details" in parts.path:
			return [uri]

		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "num-pagination-page"})
		urls = snippet.find_all("a", attrs={"class" : "title"})
		
		return [ parts._replace(path=url.get('href'), query="").geturl() for url in urls ]
			
	def get_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")
		info = AppInfo()
		info.name = soup.find('h1', attrs={"class" : "doc-banner-title"}).renderContents()
		info.category = ""
		info.version = ""
		info.size = ""
		info.updated = ""
		info.price = ""
		info.os = "Android"
		info.developer = soup.find('a', attrs={"class" : "doc-header-link"}).renderContents()
		info.language = ""
		# info.description = soup.find('div', attrs={"class" : "product-review"}).p.renderContents().replace("<br />", "\n")
		desc = soup.find(id="doc-original-text").text
		info.description = desc

		artwork = soup.find('div', attrs={"class" : "doc-banner-icon"}).img["src"]
		info.artwork = self.br.retrieve(artwork)[0]

		div_images = soup.find('div', attrs={"class" : "screenshot-carousel-content-container"})
		images = div_images.find_all('img')
		info.images = [self.br.retrieve(img["src"])[0] for img in images]

		info.debug()
		return info
