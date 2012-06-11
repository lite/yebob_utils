#!/usr/bin/env python
# coding=utf-8

import unittest
from Yebob import Yebob
from AppInfo import AppInfo

class TestYebob(unittest.TestCase):
	def setUp(self):
		self.yebob = Yebob('config.yaml')

	def test_post_app_info(self):
		info = self.new_app_info()
		product_id = self.yebob.post_app_info(info)
		assert product_id != None, "product_id is None"

	def test_upload_app_icon(self):
		info = self.new_app_info()
		info.product_id = "iwo6cpb43y"
		self.yebob.upload_app_icon(info)
		
	def new_app_info(self):
		info = AppInfo()
		info.name = "Motion Math Zoom"
		info.artwork = "test.png"
		info.category = "Education"
		info.version = "2.1"
		info.size = "19.1MB"
		info.updated = "2011-12-30"
		info.price = "Free"
		info.developer = "Motion Math"
		info.language = "English"
		info.os = "iOS"
		info.description = "An animal adventure through the world of numbers! Give your child a chance to play with numbers - they'll have a blast zooming through the number line as they master place value."
		return info

if __name__=="__main__":
	unittest.main()