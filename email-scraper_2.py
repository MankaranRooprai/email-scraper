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
emails = []

# Getting the needed urls from the user
runs = int(input("Enter the number of websites you want the emails from: "))
for i in range(runs):
    urls.append(input("Enter the url from which you want emails: "))
    
    parts = urlsplit(urls[i])
    print(parts)
    base_url = "{0.scheme}://{0.netloc}".format(parts)
    print(base_url)
    path = urls[i][:urls[i].rfind('/')+1] if '/' in parts.path else urls[i]
    print(path)

    try:
        response = requests.get(urls[i])
        print(response)
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue

    
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))

    emails.extend(new_emails)

    soup = BeautifulSoup(response.text, features="lxml")

    for anchor in soup.find_all("a"):
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''
