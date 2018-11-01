#!/usr/bin/python

from lxml import html
import requests

#url = input("Enter URL for parsing: ")

page = requests.get('https://www.crossfitinvictus.com/wod/october-25-2018-performance/')
tree = html.fromstring(page.content)

data = tree.xpath('//p/text()')

print(data)
