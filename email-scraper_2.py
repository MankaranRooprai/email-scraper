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
import time

urls = []
emails = []
masterurls = []

# Getting the needed urls from the user
runs = int(input("Enter the number of websites you want the emails from: "))

for j in range(runs):
    masterurls.append(input("Enter the url from which you want emails: "))
start = 0.0
diff = 0.0
for em in masterurls:
    urls.append(em)
    start = time.perf_counter()
    for k in urls:
        if diff <=10:
            print(diff)
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

            
            new_emails = [re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I)]

            for m in new_emails:
                for n in m:
                        
                    if n in emails:
                        continue
                    else:
                        emails.append(n)

            soup = BeautifulSoup(response.text, features="lxml")

            for anchor in soup.find_all("a"):

                link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                if link.startswith('/'):
                    link = base_url + link
                elif not link.startswith('http'):
                    link = path + link
            
                if not link in urls:
                    urls.append(link) 

            desktop_path = os.path.expanduser('~')+'\\Desktop\\emails.csv'
            print(emails)

            df = pd.DataFrame(emails, columns=["Email"])

            try:
                df.to_csv(desktop_path, index=False, header=False)
            except PermissionError:
                print('Please close the csv file.')
                break

            print(len(urls))
        else:
            urls.clear()
            
            diff = 0.0
            break
        diff = time.perf_counter() - start
        