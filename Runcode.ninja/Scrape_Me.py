#!/usr/bin/env python
#This script will accept a url as a command line argument and scrape the source html from that url.

import sys
from urllib import urlopen

#Open a connection to the url using the provided command line argument.
response = urlopen(sys.argv[1])

#Store the response as html content.
html = response.read()

#Print the html content.
print(html)
