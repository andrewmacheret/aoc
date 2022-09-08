#!/usr/bin/env python3
from pycookiecheat import chrome_cookies
import sys

url = sys.argv[1]

# Uses Chrome's default cookies filepath by default
print('; '.join(map('='.join, chrome_cookies(url).items())))
