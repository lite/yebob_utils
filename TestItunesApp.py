#!/usr/bin/env python
# coding=utf-8

import unittest
from ItunesApp import ItunesApp

class TestItunesApp(unittest.TestCase):
	def setUp(self):
		self.itunes = ItunesApp()
	
	def test_get_app_links(self):
		uri = "http://itunes.apple.com/cn/genre/ios-you-xi/id6014?mt=8"
 		links = self.itunes.get_app_links(uri)
 		assert links != None, "links is None"
		assert len(links) != 0, "len(links) is 0"
		
 	def test_get_app_info(self):
		uri = "http://itunes.apple.com/cn/app/motion-math-zoom/id451793073"
 		info = self.itunes.get_app_info(uri)
		assert info.name != None, "app name is None"
		assert info.artwork != None, "app artwork is None"
		assert info.developer != None, "app developer is None"
		assert info.description != None, "app description is None"

if __name__=="__main__":
	unittest.main()