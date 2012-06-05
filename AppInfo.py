#!/usr/bin/env python
# coding=utf-8

from urllib import urlencode
from BeautifulSoup import BeautifulSoup
from mechanize import Browser

class AppInfo:
	def get_app_info(self, uri):
		# <div rating-software="100,itunes-games" parental-rating="1" class="lockup product application">
		#  <ul class="list">
		#  <li><div class="price">免费</div></li>
		#  <li class="genre"><span class="label">类别: </span><a href="http://itunes.apple.com/cn/genre/ios-jiao-yu/id6017?mt=8">教育</a></li>
		#  <li class="release-date"><span class="label">更新: </span>2011年12月30日</li>
		#  <li><span class="label">版本: </span>2.1</li>
		#  <li><span class="label">大小： </span>19.1 MB</li>
		#  <li class="language"><span class="label">语言: </span>英语</li>
		#  <li><span class="label">开发商: </span>Motion Math</li>
		#  <li class="copyright">© 2011, Motion Math Inc.</li>
		#  </ul>
		#  <div class="app-rating"><a href="http://itunes.apple.com/WebObjects/MZStore.woa/wa/appRatings">限4岁以上</a></div>
		#  <p><span class="app-requirements">系统要求： </span>与 iPhone、iPod touch、iPad 兼容。需要 iOS 4.0 或更高版本</p>
		# </div>
		# <div class="product"><img width="175" height="175" alt="Motion Math Zoom" class="artwork" src="http://a4.mzstatic.com/us/r1000/091/Purple/e3/97/f3/mzl.fyqdmygq.175x175-75.jpg" /></div>
		br = Browser()
		res = br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data)
		self.name = soup.find('div', attrs={"id" : "title"}).h1.renderContents()
		self.artwork = soup.find('div', attrs={"id" : "left-stack"}).div.img["src"]
		self.category = "Education"
		self.version = "2.1"
		self.size = "19.1MB"
		self.updated = "2011-12-30"
		self.price = "Free"
		self.developer = soup.find('div', attrs={"id" : "title"}).h2.renderContents()
		self.language = "English"
		self.description = soup.find('div', attrs={"class" : "product-review"}).p.renderContents().replace("<br />", "\n")
		#self.debug()

	def post_app_info(self, username, password):
		#self.debug()
		br = Browser()
		fn = br.retrieve(self.artwork)[0]
		#print fn

		uri = "http://www.yebob.com/accounts/Login"
		br.open(uri)
		
		# for f in br.forms():
		#     print f

		br.select_form(nr=0)

		br.form['na']= username
		br.form['pw']= password
		br.submit()
		#print br.response().read()
		br.response().read()
		
		params = urlencode({"c":"game"})
		uri =  "http://www.yebob.com/game/product/create?%s" % (params)
		br.open(uri)
		
		# for f in br.forms():
		#     print f

		br.select_form(nr=1)

		# category_id:game
		# sname:test
		# cname:简体中文名
		# oname[]:又名
		# developer[]:开发者
		# os[]:Android
		# device[]:手机
		# lang[]:中文
		# site:www.yebob.com
		# year:2011
		# desc:简介
		# step:1
		# :test
		br.form['sname']= self.name
		br.form['cname']= self.name
		br.form['oname[]']= "又名"
		br.form['developer[]']= self.developer
		br.form['os[]']= "Android"
		br.form['device[]']= "手机"
		br.form['lang[]']= "中文"
		br.form['site']= "www.yebob.com"
		br.form['year']= "2011"
		br.form['desc']= self.description
		br.submit()
		#print br.response().read()
		br.response().read()

		br.select_form(nr=1)
		br.form.add_file(open(fn), 'image/jpeg', fn)
		br.submit()
		br.response().read()


	def debug(self):
		import sys
		reload(sys).setdefaultencoding('utf8')

		print("name: %s" % (self.name))
		print("artwork: %s" % (self.artwork))
		print("developer: %s" % (self.developer))
		print("description: %s" % (self.description))
		