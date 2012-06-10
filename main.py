#!/usr/bin/env python
# coding=utf-8

import sys 
from ItunesApp import ItunesApp
from GooglePlayApp import GooglePlayApp
from Yebob import Yebob

def usage():  
	print("%s <app_url_in_market>" %sys.argv[0]); 
	print("\t<app_url_in_market> is the app url in market or app store"); 
	print("\t         %s \"http://itunes.apple.com/cn/genre/ios-you-xi/id6014?mt=8\"" %sys.argv[0]); 
	print("\t         %s \"https://play.google.com/store/apps/category/GAME/collection/topselling_free?hl=zh_CN\"" %sys.argv[0]); 
	
def get_market(app_url):
	if "http://itunes.apple.com/" in app_url:
		return ItunesApp()

	return GooglePlayApp()

if "__main__" == __name__:  
	if len(sys.argv) != 2:  
		usage()  
		sys.exit(1)  
	
	reload(sys).setdefaultencoding('utf8')
	
	app_url = sys.argv[1]
	market = get_market(app_url)
	links = market.get_app_links(app_url)
	
	yebob = Yebob('config.yaml')
	for link in links:
		print link
		info = market.get_app_info(link)
		yebob.post_app_info(info)
		