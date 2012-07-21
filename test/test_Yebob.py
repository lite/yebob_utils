#!/usr/bin/env python
# coding=utf-8

import unittest
import sys
sys.path.append('./src')

from Yebob import Yebob
from AppInfo import AppInfo

class TestYebob(unittest.TestCase):
	def setUp(self):
		self.yebob = Yebob('./conf/config.yaml')

	def test_post_app_info(self):
		info = self.new_app_info()
		product_id = self.yebob.post_app_info(info)
		assert product_id != None, "product_id is None"

	def test_upload_app_icon(self):
		info = self.new_app_info()
		info.product_id = "iwo6cpb43y"
		self.yebob.upload_app_icon(info)
	
	def test_upload_app_images(self):
		info = self.new_app_info()
		info.images = ["https://lh3.ggpht.com/yDaXQWy-sjDXWeYhCo53duifTwOofXZn0IWC7tYQte2L9PjqBVQXLFVlwBOdg5tZ3fQ=h230",
			"https://lh3.ggpht.com/UIJYJOkg4oQsjD1eiNbEawHWyW-cBMNSOp165ndGBVLgSaPxWrTCOmafEKtTlT-56CY=h230"]
		info.product_id = "iwo6cpb43y"
		self.yebob.upload_app_images(info)
	
	def new_app_info(self):
		info = AppInfo()
		info.name = "Motion Math Zoom"
		info.category = "Education"
		info.version = "2.1"
		info.size = "19.1MB"
		info.updated = "2011-12-30"
		info.price = "Free"
		info.developer = "Motion Math"
		info.language = "English"
		info.os = "iOS"
		info.description = "<p>An animal adventure through the world of numbers! Give your child a chance to play with numbers - they'll have a blast zooming through the number line as they master place value.</p>"
		info.artwork = "https://lh3.ggpht.com/LDtlOWSOvxXBDhx4XqcBBGkANPlusko8WgB80n62bpnyTUgz34gl9OlOpmflckVNBA=h230"
		return info

if __name__=="__main__":
	unittest.main()