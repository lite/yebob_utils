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
        soup = BeautifulSoup(data, "html5lib", from_encoding="utf-8")
        info = AppInfo()
        # info.name = soup.find('h1', attrs={"class" : "doc-banner-title"}).text
        info.name = soup.find('div', attrs={"class" : "document-title"}).text
        info.category = ""
        info.version = ""
        info.size = ""
        info.updated = ""
        info.price = ""
        info.os = "Android"
        # info.developer = soup.find('a', attrs={"class" : "doc-header-link"}).text
        info.developer = soup.find('a', attrs={"class" : "document-subtitle"}).text
        info.language = ""
        # desc = soup.find(id="doc-original-text").prettify()
        desc = soup.find('div', attrs={"class" : "show-more-content"}).prettify()
        
        info.description = desc

        # artwork = soup.find('div', attrs={"class" : "doc-banner-icon"}).img["src"]
        artwork = soup.find('div', attrs={"class" : "cover-container"}).img["src"]
        info.artwork = artwork

        # div_images = soup.find('div', attrs={"class" : "screenshot-carousel-content-container"})
        div_images = soup.find('div', attrs={"class" : "thumbnails"})
        images = div_images.find_all('img')
        info.images = [img["src"] for img in images]

        info.debug()
        return info
