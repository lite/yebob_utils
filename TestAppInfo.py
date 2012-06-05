#!/usr/bin/env python
# coding=utf-8

import unittest
from AppInfo import AppInfo

class TestAppInfo(unittest.TestCase):

	def test_get_app_info(self):
		info = AppInfo()
		uri = "http://itunes.apple.com/cn/app/motion-math-zoom/id451793073"
 		info.get_app_info(uri)
		assert info.name != None, "app name is None"
		assert info.artwork != None, "app artwork is None"
		assert info.developer != None, "app developer is None"
		assert info.description != None, "app description is None"

	def test_post_app_info(self):
		username = ""
		password = ""
		self.new_app_info().post_app_info(username, password)
	
	def test_debug(self):
		self.new_app_info().debug()

	def new_app_info(self):
		info = AppInfo()
		info.name = "Motion Math Zoom"
		info.artwork = "http://a4.mzstatic.com/us/r1000/091/Purple/e3/97/f3/mzl.fyqdmygq.175x175-75.jpg"
		info.category = "Education"
		info.version = "2.1"
		info.size = "19.1MB"
		info.updated = "2011-12-30"
		info.price = "Free"
		info.developer = "Motion Math"
		info.language = "English"
		info.description = "An animal adventure through the world of numbers! Give your child a chance to play with numbers - they'll have a blast zooming through the number line as they master place value."
		return info

if __name__=="__main__":
	unittest.main()