#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Volker Ka.'
SITENAME = 'Silverian Adventures'
SITEURL = ''

TIMEZONE = 'Europe/Paris'
PLUGIN_PATH = "pelican-plugins/"
PLUGINS = ["render_math"]

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/home/vsilv/Programming/blog/pelican/themes/pure"
COVER_IMG_URL = "http://www.nationalgeographic.de/static/images/wallpaper/hildur-runs-to-simba-east_1600.jpg"
COVER_IMG_URL = "http://www.nationalgeographic.de/static/images/wallpaper/colville-indian-reservation-washington-1600.jpg"
