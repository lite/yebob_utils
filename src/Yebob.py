#!/usr/bin/env python
# coding=utf-8

import tempfile,yaml
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
        sname = info.name[0:50]
        self.br.form['sname']= sname
        self.br.form['cname']= sname
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
        self.br.select_form(nr=1)
        info.product_id = self.br.form["product_id"]
        info.product_id
        
        # upload_app_icon
        #img = self.down_image(info.artwork)
        #self.br.form.find_control(type='file').add_file(open(img), 'image/jpeg', img)
        #self.br.submit().read()
        self.upload_app_icon(info)
    
        # upload_app_images
        self.upload_app_images(info)
        
    def upload_app_icon(self, info):
        uri = "http://www.yebob.com/game/product/update-logo?product_id=%s" % (info.product_id)
        self.upload_image(uri, self.down_image(info.artwork))
      
    def down_image(self, img):
        print "down image from " + img
        down_br = Browser()
        down_cj = CookieJar()
        down_br.set_cookiejar(down_cj)
        fn = tempfile.mktemp(suffix='.png')
        return down_br.retrieve(img, filename = fn)[0]
        
    def upload_app_images(self, info):
		uri = "http://www.yebob.com/game/product/add-photos?product_id=%s" % (info.product_id)
		for img in info.images:
			self.upload_image(uri, self.down_image(img))
	
    def upload_image(self, uri, img):
		print "upload %s to %s" %(img, uri)
		self.br.open(uri).read()
		self.br.select_form(nr=1)
		self.br.form.find_control(type='file').add_file(open(img), 'image/png', img)
		self.br.submit().read()
