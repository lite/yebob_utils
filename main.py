#!/usr/bin/env python
# coding=utf-8

import sys 
from ItunesApp import ItunesApp
from Yebob import Yebob

def usage():  
	print("%s <app_url_in_market>" %sys.argv[0]); 
	print("\t<app_url_in_market> is the app url in market or app store"); 
	print("\t         %s \"http://itunes.apple.com/cn/genre/ios-you-xi/id6014?mt=8\"" %sys.argv[0]); 
  
if "__main__" == __name__:  
	if len(sys.argv) != 2:  
		usage()  
		sys.exit(1)  
	
	reload(sys).setdefaultencoding('utf8')
	
	yebob = Yebob('config.yaml')
	itunes = ItunesApp()
	links = itunes.get_app_links(sys.argv[1])

	for link in links:
		print link
		info = itunes.get_app_info(link)
		yebob.post_app_info(info)
		break
