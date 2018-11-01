#!/usr/bin/python

import urllib.request
import re

url = input("Enter URL for parsing: ")

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

data = re.findall(r'<p>(.*?)</p>',str(respData))

print(data)
