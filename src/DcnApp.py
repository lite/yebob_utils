#!/usr/bin/env python
# coding=utf-8

import re, urlparse
from bs4 import BeautifulSoup, Comment
from mechanize import Browser
from AppInfo import AppInfo

class DcnApp:
	def __init__(self):
		self.br = Browser()
		self.br.addheaders = [("HTTP_CONNECTION", "keep-alive"),]
	
	def get_app_links(self, uri):
		parts = urlparse.urlparse(uri)
		if "android.d.cn" in parts.netloc:
			return self.get_android_app_links(uri)
		elif "ios.d.cn" in parts.netloc:
			return self.get_ios_app_links(uri)
		elif "wp.d.cn" in parts.netloc:
			return self.get_wp_app_links(uri)

	def get_app_info(self, uri):
		parts = urlparse.urlparse(uri)
		if "android.d.cn" in parts.netloc:
			return self.get_android_app_info(uri)
		elif "ios.d.cn" in parts.netloc:
			return self.get_ios_app_info(uri)
		elif "wp.d.cn" in parts.netloc:
			return self.get_wp_app_info(uri)

	def get_app_pages(self, uri):
		parts = urlparse.urlparse(uri)
		if "android.d.cn" in parts.netloc:
			return self.get_android_app_pages(uri)
		elif "ios.d.cn" in parts.netloc:
			return self.get_ios_app_pages(uri)
		elif "wp.d.cn" in parts.netloc:
			return self.get_wp_app_pages(uri)

	def get_url(self, uri, new_path):
		return urlparse.urlparse(uri)._replace(path=new_path).geturl();

	def get_wp_app_pages(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find(id="ctl00_ContentPlaceHolder1_ctl00_pager")
		urls = snippet.find_all("a")
		
		return list(set([uri] + [ self.get_url(uri, url.get('href')) for url in urls ]))
	
	def get_wp_app_links(self, uri):
		m = re.search(r"/\d+_.+.html", uri)
		if m is not None:
			return [uri]

		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		div_lists = soup.find('div', attrs={"class" : "listsoga"})
		urls = div_lists.find_all("a")
		
		return list(set([ self.get_url(uri, url.get('href')) for url in urls ]))

	def get_wp_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")

		info = AppInfo()
		div_viewbox = soup.find('div', attrs={"class" : "info"})
		info.name = div_viewbox.h1.text.strip()
		info.category = ""
		info.version = ""
		info.size = ""
		info.updated = ""
		info.price = ""
		info.os = "iOS"
		info.developer = ""
		info.language = ""
		desc = soup.find(id="discription").prettify() # not description
		info.description = desc

		artwork = soup.find('div', attrs={"class" : "deinfo"}).img["src"]
		info.artwork = self.get_url(uri, artwork)
		
		div_images = soup.find('div', attrs={"class" : "screenshots-container"})
		images = div_images.find_all('img')
		info.images = [self.get_url(uri, img["src"]) for img in images]

		info.debug()
		return info
	
	def get_ios_app_pages(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "page"})
		urls = snippet.find_all("a")
		
		return list(set([ self.get_url(uri, url.get('href')) for url in urls ]))

	def get_ios_app_links(self, uri):
		m = re.search(r"(-list)?-\d+.html", uri)
		if m is not None:
			if m.group(1) is None:
				return [uri]

		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		div_mtop10 = soup.find("div", attrs={"class" : "yylb_mid"})
		urls = div_mtop10.find_all("a")
		
		return list(set([ self.get_url(uri, url.get('href')) for url in urls ]))

	def get_ios_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")

		info = AppInfo()
		info.name = soup.find(id="appTitle").text.strip()
		info.category = ""
		info.version = ""
		info.size = ""
		info.updated = ""
		info.price = ""
		info.os = "iOS"
		info.developer = ""
		info.language = ""
		desc = soup.find(id="tab2Content").prettify()
		info.description = desc

		artwork = soup.find('img', attrs={"class" : "img175"})["src"]
		info.artwork = self.get_url(uri, artwork)
		
		div_images = soup.find('div', attrs={"class" : "yyxq_yyjt"})
		images = div_images.find_all('img')
		info.images = [self.get_url(uri, img["src"]) for img in images]

		info.debug()
		return info
	
	def get_android_app_pages(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "pager"})
		urls = snippet.find_all("a")
		
		return list(set([ self.get_url(uri, url.get('href')) for url in urls ]))

	def get_android_app_links(self, uri):
		parts = urlparse.urlparse(uri)
		if ".html" in parts.path:
			return [uri]

		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		urls = soup.find_all("a", attrs={"class" : "gamesoft_link"})
		
		return list(set([ self.get_url(uri, url.get('href')) for url in urls ]))

	def get_android_app_info(self, uri):
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
		info.os = "Android"
		info.developer = ""
		info.language = ""
		desc = soup.find('div', attrs={"class" : "rom_introductioncon yingyong_intro"}).prettify()
		info.description = desc

		artwork = soup.find('div', attrs={"class" : "yingyong_img"}).img["src"]
		info.artwork = artwork
		
		div_images = soup.find('div', attrs={"class" : "snapshot_list"})
		images = div_images.find_all('img')
		info.images = [img["src"] for img in images]

		info.debug()
		return info
	