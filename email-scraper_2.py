from email.mime import base
import imp
from operator import imod
from traceback import print_tb
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re
import pandas as pd
import os
import sys

urls = []
emails = []

# Getting the needed urls from the user
runs = int(input("Enter the number of websites you want the emails from: "))

for j in range(runs):
    urls.append(input("Enter the url from which you want emails: "))

while len(urls) <= 100:

    for k in urls:
        parts = urlsplit(k)
        #print(parts)
        base_url = "{0.scheme}://{0.netloc}".format(parts)
        #print(base_url)
        path = k[:k.rfind('/')+1] if '/' in parts.path else k
        #print(path)

        try:
            response = requests.get(k) 
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
            continue

        
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))

        if new_emails in emails:
            continue
        else:
            emails.extend(new_emails)

        soup = BeautifulSoup(response.text, features="lxml")

        for anchor in soup.find_all("a"):

            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
            if link.startswith('/'):
                link = base_url + link
            elif not link.startswith('http'):
                link = path + link
        
            if not link in urls:
                urls.append(link) 


        print(emails)

        df = pd.DataFrame(emails, columns=["Email"])
        desktop_path = os.path.expanduser('~')+'\\Desktop\\emails.csv'

        try:
            df.to_csv(desktop_path, mode='a', index=False, header=False)
        except PermissionError:
            print('Please close the csv file.')

        print(len(urls))