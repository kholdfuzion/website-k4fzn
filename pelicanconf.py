#!/usr/bin/env python3
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'K4FZN Larry'
SITENAME = u'K4FZN Labs'
SITEURL = 'k4fzn.net'
THEME = "themes/Flex"
PATH = 'content'

STATIC_PATHS = ['images', 'icons', 'feeds']

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

LINKS = (
        ('NCMesh', 'http://ncmesh.net'),
        ('YouTube', 'http://youtube.com/@k4fzn'),
        ('Github', 'http://github.com/kholdfuzion')

)

