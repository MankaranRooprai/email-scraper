import imp
from operator import imod
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re

urls = set()
# Getting the needed urls from the user
runs = int(input("Enter the number of websites you want the emails from: "))
for i in range(runs):
    urls.add(input("Enter the url from which you want emails: "))

