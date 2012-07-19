#!/usr/bin/env python
# coding=utf-8

import sys, unittest
from YebobDoc import YebobDoc
from mechanize import Browser
from bs4 import BeautifulSoup

class TestYebobDoc(unittest.TestCase):
	def setUp(self):
		self.doc = YebobDoc()

	def test_from_html_with_br(self):
		txt = self.doc.from_html("<p>hello<br/>word</p>")
		assert txt != None, "txt is None."

	def test_from_html_with_comments(self):
		txt = self.doc.from_html("<p>hello <!--this is comments--> word</p>")
		assert txt != None, "txt is None."

	def test_from_bs4(self):
		br = Browser()
		br.addheaders = [("HTTP_CONNECTION", "keep-alive")]
		uri = "http://itunes.apple.com/cn/app/toca-robot-lab/id434826169?mt=8"
		res = br.open(uri)
		data = res.get_data() 
		soup = BeautifulSoup(data, "html5lib")
		div_desc = soup.find('div', attrs={"class" : "product-review"})
		# print type(div_desc), div_desc.get_text(), div_desc.prettify()
		txt = self.doc.from_html(div_desc.prettify())
		# print txt
		assert txt != None, "txt is None."

if __name__=="__main__":
	reload(sys).setdefaultencoding('utf8')
	unittest.main()