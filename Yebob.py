#!/usr/bin/env python
# coding=utf-8

import yaml
from urllib import urlencode
from BeautifulSoup import BeautifulSoup
from mechanize import Browser

class Yebob:
	def __init__(self, config):
		config = yaml.load(file(config, 'r'))
		username = config["user"]
		password = config["pass"]

		self.br = Browser()
		uri = "http://www.yebob.com/accounts/Login"
		self.br.open(uri)
		self.br.select_form(nr=0)
		self.br.form['na']= username
		self.br.form['pw']= password
		self.br.submit()
		self.br.response().read()
		
	def post_app_info(self, info):
		params = urlencode({"c":"game"})
		uri =  "http://www.yebob.com/game/product/create?%s" % (params)
		self.br.open(uri)
		self.br.select_form(nr=1)
		self.br.form['sname']= info.name
		self.br.form['cname']= info.name
		self.br.form['oname[]']= "又名"
		self.br.form['developer[]']= info.developer
		self.br.form['os[]']= "Android"
		self.br.form['device[]']= "手机"
		self.br.form['lang[]']= "中文"
		self.br.form['site']= "www.yebob.com"
		self.br.form['year']= "2011"
		self.br.form['desc']= info.description
		self.br.submit()
		self.br.response().read()
		self.br.select_form(nr=1)
		self.br.form.add_file(open(info.artwork), 'image/jpeg', info.artwork)
		self.br.submit()
		self.br.response().read()
