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
		assert info.developer != None, "app developer is None"
		assert info.description != None, "app description is None"

	def test_get_app_info(self):
		info = AppInfo()
		uri = "http://itunes.apple.com/cn/app/motion-math-zoom/id451793073"
 		info.get_app_info(uri)
		info.post_app_info("username", "password")
	
if __name__=="__main__":
	unittest.main()