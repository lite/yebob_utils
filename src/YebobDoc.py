#!/usr/bin/env python
# coding=utf-8

import html2text

class YebobDoc:

	def __init__(self):
		self.h = html2text.HTML2Text()
		self.h.ignore_links = True

	def from_html(self, html):
		return self.h.handle(html).strip()