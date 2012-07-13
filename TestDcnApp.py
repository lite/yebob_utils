#!/usr/bin/env python
# coding=utf-8

import unittest
from DcnApp import DcnApp

class TestDcnApp(unittest.TestCase):
	def setUp(self):
		self.market = DcnApp()

	def test_get_app_pages(self):
		uri = "http://android.d.cn/game/"
		pages = self.market.get_app_pages(uri)
 		print pages
 		assert pages != None, "pages is None"
		assert len(pages) != 0, "len(pages) is 0"
		
	def test_get_app_links(self):
		uri = "http://android.d.cn/game/rpg_0_all_all_update_7/"
		links = self.market.get_app_links(uri)
 	  	assert links != None, "links is None"
		assert len(links) != 0, "len(links) is 0"
		
 	def test_get_app_info(self):
		uri = "http://android.d.cn/game/8213.html"
 		info = self.market.get_app_info(uri)
		assert info.name != None, "app name is None"
		assert info.artwork != None, "app artwork is None"
		assert info.developer != None, "app developer is None"
		assert info.description != None, "app description is None"

if __name__=="__main__":
	unittest.main()