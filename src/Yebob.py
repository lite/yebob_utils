#!/usr/bin/env python
# coding=utf-8

import yaml
from urllib import urlencode
from mechanize import Browser, CookieJar
from YebobDoc import YebobDoc

class Yebob:
  def __init__(self, config):
		self.doc = YebobDoc()

		self.br = Browser()
		self.cj = CookieJar()
		self.br.set_cookiejar(self.cj)
		self.br.addheaders = [("HTTP_CONNECTION", "keep-alive")]

		config = yaml.load(file(config, 'r'))
		username = config["user"]
		password = config["pass"]

		uri = "http://www.yebob.com/accounts/Login"
		print uri
		self.br.open(uri).read()
		self.br.select_form(nr=0)
		self.br.form['na']= username
		self.br.form['pw']= password
		self.br.submit().read()	
  
  def post_app_info(self, info):
    uri =  "http://www.yebob.com/game/product/create"
    print uri
    self.br.open(uri).read()
    self.br.select_form(nr=1)
    self.br.form['sname']= info.name
    self.br.form['cname']= info.name
    developer = info.developer[0:30]
    self.br.form['developer[]']= developer
    desc = self.doc.from_html(info.description)
    self.br.form['desc']= desc
    self.br.form['oname[]']= ""
    self.br.form['os[]']= info.os
    self.br.form['device[]']= "手机"
    self.br.form['lang[]']= "中文"
    self.br.form['site']= ""
    self.br.form['year']= ""
    self.br.submit().read()
  
    # http://www.yebob.com/game/product/edit?id=iuqftrcvmg&type=params
    # upload_app_icon
    img = self.down_image(info.artwork)
    self.br.select_form(nr=1)
    info.product_id = self.br.form["product_id"]
    print info.product_id
    self.br.form.find_control(type='file').add_file(open(img), 'image/jpeg', img)
    self.br.submit().read()
    
    # upload_app_images
    self.upload_app_images(info)
        
  def down_image(self, img):
		print "down image from " + img
		down_br = Browser()
		down_cj = CookieJar()
		down_br.set_cookiejar(down_cj)
		return down_br.retrieve(img)[0]
        
  def upload_app_images(self, info):
		uri = "http://www.yebob.com/game/product/add-photos?product_id=%s" % (info.product_id)
		for img in info.images:
			self.upload_image(uri, self.down_image(img))
	
  def upload_image(self, uri, img):
		print "upload %s to %s" %(img, uri)
		self.br.open(uri).read()
		self.br.select_form(nr=1)
		self.br.form.find_control(type='file').add_file(open(img), 'image/jpeg', img)
		self.br.submit().read()