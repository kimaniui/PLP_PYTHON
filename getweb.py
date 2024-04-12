#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 22:00
# @Author  : Kimani 
#program to download a website and all its contents to the hard disk using python

import os   
import requests
from bs4 import BeautifulSoup

def download(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.find_all("a"):
        href = link.get("href")
        if href == None:
            continue
        if href.startswith("http"):
            pass
        else:
            href = url + href
        if href.endswith("/"):
            if not os.path.exists(os.path.basename(href)):
                os.mkdir(os.path.basename(href))
            download(href)
        else:
            response = requests.get(href)
            with open(os.path.basename(href), "wb") as file:
                file.write(response.content)
            print(href)

if __name__ == "__main__":
    url = input("Enter the URL: ")
    download(url)
    print("Download complete!")

#The program uses the requests module to download the website and the BeautifulSoup module to parse the HTML content of the website.