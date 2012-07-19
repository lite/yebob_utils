#!/usr/bin/env python
# coding=utf-8

class AppInfo:
	name = ""
	artwork = ""
	category = ""
	version = ""
	size = ""
	updated = ""
	price = ""
	developer = ""
	language = ""
	description = ""
	images = []

	def debug(self):
		print("name: %s" % (self.name))
		print("artwork: %s" % (self.artwork))
		print("developer: %s" % (self.developer))
		print("description: %s" % (self.description))

		print("images:")
		for img in self.images:
			print("\t%s" % (img))
	