#!/usr/bin/env python
# coding=utf-8

import unittest
from WinPhoneApp import WinPhoneApp

class TestWinPhoneApp(unittest.TestCase):
	def setUp(self):
		self.market = WinPhoneApp()
		
	def test_get_app_links(self):
		uri = "http://www.windowsphone.com/zh-CN/categories/actionandadventure?list=top"
 		links = self.market.get_app_links(uri)
 		print links
 		assert links != None, "links is None"
		assert len(links) != 0, "len(links) is 0"
	
	def test_get_app_links_by_developer(self):
		uri = "http://www.windowsphone.com/zh-CN/publishers/Hexage"
 		links = self.market.get_app_links(uri)
 		print links
 		assert links != None, "links is None"
		assert len(links) != 0, "len(links) is 0"
		
 	def test_get_app_info(self):
 		uri = "http://www.windowsphone.com/zh-CN/apps/4a9e9b87-ccd8-4c95-8eef-846bfadc6e1e"
 		info = self.market.get_app_info(uri)
		assert info.name != None, "app name is None"
		assert info.artwork != None, "app artwork is None"
		assert info.developer != None, "app developer is None"
		assert info.description != None, "app description is None"

if __name__=="__main__":
	unittest.main()