#!/usr/bin/env python
# coding=utf-8

import urlparse
from bs4 import BeautifulSoup
from mechanize import Browser
from AppInfo import AppInfo

class ItunesApp:

    def __init__(self):
        self.br = Browser()
        self.br.addheaders = [("HTTP_CONNECTION", "keep-alive")]

    def get_app_links(self, uri):
        parts = urlparse.urlparse(uri)
        if "/app/" in parts.path:
            return [uri]

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
        info.name = soup.find(id="desktopContentBlockId").h1.renderContents()
        info.category = ""
        info.version = ""
        info.size = ""
        info.updated = ""
        info.price = ""
        info.os = "iOS"
        developer = soup.find(id="desktopContentBlockId").h2.renderContents()
        info.developer = developer.split("：")[1] if "：" in developer else developer
        info.language = ""
        desc = soup.find('div', attrs={"class" : "product-review"}).p.prettify()
        info.description = desc
		
        artwork = soup.find(id="left-stack").div.img["src"]
        info.artwork = artwork
		
        div_images = soup.find('div', attrs={"class" : "screenshots"})
        images = div_images.find_all('img')
        info.images = [img["src"] for img in images]

        info.debug()
        return info
