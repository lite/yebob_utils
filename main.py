#!/usr/bin/env python
# coding=utf-8

import sys 
from AppInfo import AppInfo

def usage():  
	print("%s <app_url_in_market>" %sys.argv[0]); 
	print("\t<app_url_in_market> is the app url in market or app store"); 
	print("\texample: %s http://itunes.apple.com/cn/app/motion-math-zoom/id451793073" %sys.argv[0]); 
  
if "__main__" == __name__:  
	if len(sys.argv) != 2:  
		usage()  
		sys.exit(1)  

	username = ""
	password = ""
	print "%s %s" % (sys.argv[0], sys.argv[1])
	info = AppInfo()
	info.get_app_info(sys.argv[1]);
	info.post_app_info(username, password)