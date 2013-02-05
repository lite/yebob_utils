#!/usr/bin/env python
# coding=utf-8

import re

class YebobDoc:
    def from_html(self, html):
        text = re.sub("<.+>\s*", "", html)
        text = re.sub("</.+>\s*", "", text)
        text = re.sub('(<br/?>\s*)+', '\n', text)
        text = re.sub('&nbsp;', ' ', text)
        return text