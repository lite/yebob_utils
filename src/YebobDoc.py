#!/usr/bin/env python
# coding=utf-8

import html2text
import re

class YebobDoc:

    def __init__(self):
        self.h = html2text.HTML2Text()
        self.h.ignore_links = True

    def from_html(self, html):
        text = self.h.handle(html).strip()
        strs = re.compile("\n+").split(text)
        return "\n".join(strs)