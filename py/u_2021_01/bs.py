#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

#f = open('kuji.html', 'r')
#data = f.read()
#print(data)

url = "https://rakucoin.appspot.com/rakuten/kuji/"
f = urllib.request.urlopen(url)
html = f.read().decode('utf-8')
#print(html)

soup = BeautifulSoup(html, 'html.parser')
#print('td: ', soup.td.string)

a_list = soup.find_all("a")
#print(soup.find_all("a"))

print("lstURL = [")
for a in a_list:
    href = a.get("href")
    href.strip()
    print("    # ", a.string)
    print('    "{0}",'.format(href))
#    print("    ", '"', a.get("href"), '",')
#    print(a.string)
#    print(a.get("href"))

print("]\n")

f.close()

# ends here.
