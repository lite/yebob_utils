#!/usr/bin/env python
# coding=utf-8

import sys
import urlparse
from ItunesApp import ItunesApp
from GooglePlayApp import GooglePlayApp
from Www51ipaApp import Www51ipaApp
from DcnApp import DcnApp
from Yebob import Yebob

def usage():  
	print("%s <app_url_in_market>" %sys.argv[0]); 
	print("\t<app_url_in_market> is the app url in market or app store"); 
	print
	print("market lists:")
	print
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
	print("+ d.cn")
	print("http://android.d.cn/game/"); 
	print("http://android.d.cn/game/rpg_0_all_all_update_7/"); 
	print("http://android.d.cn/game/8213.html"); 
	print
	print("- windowsphone.com")
	print("http://www.windowsphone.com/zh-CN/games?list=top"); 
	print("http://www.windowsphone.com/zh-CN/categories/actionandadventure")
	print("http://www.windowsphone.com/zh-CN/publishers/成都维动科技有限责任公司")
	print("http://www.windowsphone.com/zh-CN/apps/4a9e9b87-ccd8-4c95-8eef-846bfadc6e1e"); 
		
def get_market(uri):
	parts = urlparse.urlparse(uri)
	if "itunes.apple.com" in parts.netloc:
		return ItunesApp()
	elif "play.google.com" in parts.netloc:
		return GooglePlayApp()
	elif "www.51ipa.com" in parts.netloc:
		return Www51ipaApp()
	elif ".d.cn" in parts.netloc:
		return DcnApp()

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
		