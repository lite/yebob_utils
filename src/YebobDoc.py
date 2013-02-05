#!/usr/bin/env python
# coding=utf-8

import re

class YebobDoc:
    def from_html(self, html):
        text = re.sub("<.+>\n", "", html)
        text = re.sub("</.+>\n", "", text)
        text = re.sub('(<br/?>\s*)+', '\n', text)
        text = re.sub('&nbsp;', ' ', text)
        return text