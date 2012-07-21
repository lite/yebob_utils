#!/usr/bin/env python
# coding=utf-8

import unittest
import sys
sys.path.append('./src')

from Www51ipaApp import Www51ipaApp

class TestWww51ipaApp(unittest.TestCase):
	def setUp(self):
		self.market = Www51ipaApp()

	def test_get_app_pages(self):
		uri = "http://www.51ipa.com/games/rpg/"
 		pages = self.market.get_app_pages(uri)
 		print pages
 		assert pages != None, "pages is None"
		assert len(pages) != 0, "len(pages) is 0"
		
	def test_get_app_links(self):
		uri = "http://www.51ipa.com/games/rpg/list_5_2.html"
 		links = self.market.get_app_links(uri)
 		assert links != None, "links is None"
		assert len(links) != 0, "len(links) is 0"
		
 	def test_get_app_info(self):
 		uri = "http://www.51ipa.com/games/rpg/PiPHero-iPhone.html"
 		info = self.market.get_app_info(uri)
		assert info.name != None, "app name is None"
		assert info.artwork != None, "app artwork is None"
		assert info.developer != None, "app developer is None"
		assert info.description != None, "app description is None"

if __name__=="__main__":
	unittest.main()