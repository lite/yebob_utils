#!/usr/bin/env python
# coding=utf-8

import unittest
from GooglePlayApp import GooglePlayApp

class TestGooglePlayApp(unittest.TestCase):
	def setUp(self):
		self.market = GooglePlayApp()

	def test_get_app_links(self):
		uri = "https://play.google.com/store/apps/category/GAME/collection/topselling_free?hl=zh_CN"
 		links = self.market.get_app_links(uri)
 		assert links != None, "links is None"
		assert len(links) != 0, "len(links) is 0"
		
	def test_get_links_by_developer(self):
		uri = "https://play.google.com/store/apps/developer?id=GoodTeam"
		links = self.market.get_app_links(uri)
		assert links != None, "links is None"
		assert len(links) != 0, "len(links) is 0"
		
 	def test_get_app_info(self):
 		uri = "https://play.google.com/store/apps/details?id=com.feelingtouch.racingcar"
 		info = self.market.get_app_info(uri)
		assert info.name != None, "app name is None"
		assert info.artwork != None, "app artwork is None"
		assert info.developer != None, "app developer is None"
		assert info.description != None, "app description is None"

if __name__=="__main__":
	unittest.main()