# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# sample URL (Answer = 2553) url = "http://py4e-data.dr-chuck.net/comments_42.html"
url = "http://py4e-data.dr-chuck.net/comments_707170.html"
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Operators
count = 0
sum = 0

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    x = int(tag.contents[0])
    count += 1
    sum = sum + x
print(sum)
print(count)
