from email.mime import base
import imp
from operator import imod
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re

urls = []
# Getting the needed urls from the user
runs = int(input("Enter the number of websites you want the emails from: "))
for i in range(runs):
    urls.append(input("Enter the url from which you want emails: "))
    
    parts = urlsplit(urls[i])
    print(parts)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    print(base_url)