#!/usr/bin/env python
# coding=utf-8

import sys 
from ItunesApp import ItunesApp
from GooglePlayApp import GooglePlayApp
from Www51ipaApp import Www51ipaApp
from Yebob import Yebob

def usage():  
	print("%s <app_url_in_market>" %sys.argv[0]); 
	print("\t<app_url_in_market> is the app url in market or app store"); 
	print
	print("market lists:")
	print("+ itunes.apple.com")
	print("http://itunes.apple.com/cn/genre/ios-you-xi/id6014?mt=8"); 
	print("http://itunes.apple.com/cn/app/toca-robot-lab/id434826169?mt=8"); 
	print
	print("+ play.google.com")
	print("https://play.google.com/store/apps/category/GAME/collection/topselling_free?hl=zh_CN"); 
	print("https://play.google.com/store/apps/details?id=com.catstudio.soldierofglorycnzh"); 
	print("https://play.google.com/store/apps/developer?id=GoodTeam"); 
	print
	print("+ 51ipa.com")
	print("http://www.51ipa.com/games/rpg/"); 
	print("http://www.51ipa.com/games/rpg/PiPHero-iPhone.html"); 
	print
	print("- d.cn")
	print("http://android.d.cn/game/"); 
	print("http://android.d.cn/game/rpg_0_all_all_update_7/"); 
	print("http://android.d.cn/game/8213.html"); 
		
def get_market(app_url):
	if "http://itunes.apple.com/" in app_url:
		return ItunesApp()
	elif "https://play.google.com/store/apps/" in app_url:
		return GooglePlayApp()
	elif "http://www.51ipa.com/games/" in app_url:
		return Www51ipaApp()

def get_links(market, app_url):
	if "http://itunes.apple.com/" in app_url:
		if "/genre/" in app_url:
			return market.get_app_links(app_url)
	elif "https://play.google.com/store/apps/" in app_url:
		if "/category/" in app_url:
			return market.get_app_links(app_url)
		elif "/developer?id=" in app_url:
			return market.get_app_links(app_url)
	elif "http://www.51ipa.com/games/" in app_url:
		if ".html" in app_url:
			return market.get_app_links(app_url)
	return [app_url]
	
if "__main__" == __name__:  
	if len(sys.argv) != 2:  
		usage()  
		sys.exit(1)  
	
	reload(sys).setdefaultencoding('utf8')
	
	app_url = sys.argv[1]
	market = get_market(app_url)
	links = get_links(market, app_url)

	yebob = Yebob('config.yaml')
	for link in links:
		print link
		info = market.get_app_info(link)
		yebob.post_app_info(info)
		