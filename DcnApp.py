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

	def get_wp_app_pages(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find(id="ctl00_ContentPlaceHolder1_ctl00_pager")
		urls = snippet.find_all("a")
		
		parts = urlparse.urlparse(uri)
		return list(set([uri] + [ parts._replace(path=url.get('href')).geturl() for url in urls ]))
	
	def get_wp_app_links(self, uri):
		m = re.search(r"/\d+_.+.html", uri)
		if m is not None:
			return [uri]

		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		div_lists = soup.find('div', attrs={"class" : "listsoga"})
		urls = div_lists.find_all("a")
		
		parts = urlparse.urlparse(uri)
		return list(set([ parts._replace(path=url.get('href')).geturl() for url in urls ]))

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
		desc = soup.find(id="discription").text # not description
		info.description = desc.strip()


		parts = urlparse.urlparse(uri)
		artwork = soup.find('div', attrs={"class" : "deinfo"}).img["src"]
		info.artwork = self.br.retrieve(parts._replace(path=artwork).geturl())[0]
		
		div_images = soup.find('div', attrs={"class" : "screenshots-container"})
		images = div_images.find_all('img')
		info.images = [self.br.retrieve(parts._replace(path=img["src"]).geturl())[0] for img in images]

		info.debug()
		return info
	
	def get_ios_app_pages(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "page"})
		urls = snippet.find_all("a")
		
		parts = urlparse.urlparse(uri)
		return list(set([uri] + [ parts._replace(path=url.get('href')).geturl() for url in urls ]))

	def get_ios_app_links(self, uri):
		m = re.search(r"(-list)?-\d+.html", uri)
		if m is not None:
			if m.group(1) is None:
				return [uri]

		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		div_mtop10 = soup.find("div", attrs={"class" : "listcon"})
		urls = div_mtop10.find_all("a")
		
		parts = urlparse.urlparse(uri)
		return list(set([ parts._replace(path=url.get('href')).geturl() for url in urls ]))
	
	def get_ios_app_info(self, uri):
		res = self.br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")

		info = AppInfo()
		div_viewbox = soup.find('div', attrs={"class" : "detabt"})
		info.name = div_viewbox.h1.text.strip()
		info.category = ""
		info.version = ""
		info.size = ""
		info.updated = ""
		info.price = ""
		info.os = "iOS"
		info.developer = ""
		info.language = ""
		desc = soup.find(id="description").text
		info.description = desc.strip()

		artwork = soup.find('div', attrs={"class" : "detatu"}).img["src"]
		info.artwork = self.br.retrieve(artwork)[0]
		
		div_images = soup.find('div', attrs={"class" : "screenshots-container"})
		images = div_images.find_all('img')
		info.images = [self.br.retrieve(img["src"])[0] for img in images]

		info.debug()
		return info
	
	def get_android_app_pages(self, uri):
		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		snippet = soup.find('div', attrs={"class" : "pager"})
		urls = snippet.find_all("a")
		
		parts = urlparse.urlparse(uri)
		return list(set([uri] + [ parts._replace(path=url.get('href')).geturl() for url in urls ]))

	def get_android_app_links(self, uri):
		parts = urlparse.urlparse(uri)
		if ".html" in parts.path:
			return [uri]

		res = self.br.open(uri)
		data = res.get_data()
		soup = BeautifulSoup(data, "html5lib")
		urls = soup.find_all("a", attrs={"class" : "gamesoft_link"})
		
		return [ parts._replace(path=url.get('href')).geturl() for url in urls ]

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
		desc = soup.find('div', attrs={"class" : "rom_introductioncon yingyong_intro"}).text
		info.description = desc

		artwork = soup.find('div', attrs={"class" : "yingyong_img"}).img["src"]
		info.artwork = self.br.retrieve(artwork)[0]
		
		div_images = soup.find('div', attrs={"class" : "snapshot_list"})
		images = div_images.find_all('img')
		info.images = [self.br.retrieve(img["src"])[0] for img in images]

		info.debug()
		return info
	