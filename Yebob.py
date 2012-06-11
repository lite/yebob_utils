#!/usr/bin/env python
# coding=utf-8

import yaml
import re
from urllib import urlencode
from mechanize import Browser

class Yebob:
	def __init__(self, config):
		self.br = Browser()
		self.br.addheaders = [("HTTP_CONNECTION", "keep-alive")]

		config = yaml.load(file(config, 'r'))
		username = config["user"]
		password = config["pass"]

		uri = "http://www.yebob.com/accounts/Login"
		self.br.open(uri)
		self.br.select_form(nr=0)
		self.br.form['na']= username
		self.br.form['pw']= password
		self.br.submit().read()
		
	def post_app_info(self, info):
		params = urlencode({"c":"game"})
		uri =  "http://www.yebob.com/game/product/create?%s" % (params)
		self.br.open(uri).read()
		self.br.select_form(nr=1)
		self.br.form['sname']= info.name
		self.br.form['cname']= info.name
		developer = info.developer[0:30] 
		self.br.form['developer[]']= developer
		desc = re.sub("<(br|p)\s*/>", "\n", info.description)
		self.br.form['desc']= desc
		self.br.form['oname[]']= ""
		self.br.form['os[]']= info.os
		self.br.form['device[]']= "手机"
		self.br.form['lang[]']= "中文"
		self.br.form['site']= ""
		self.br.form['year']= ""
		self.br.submit().read()
		self.br.select_form(nr=1)
		info.product_id = self.br.form["product_id"]
		print info.product_id
		self.upload_app_icon(info)
		return info.product_id
		
	def upload_app_icon(self, info):
		uri = "http://www.yebob.com/game/product/update-logo?product_id=%s" % (info.product_id)
		self.br.open(uri).read()
		self.br.select_form(nr=1)
		self.br.form.add_file(open(info.artwork), 'image/jpeg', info.artwork, name='file')
		self.br.submit().read()
		