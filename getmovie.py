#!/usr/bin/python3
# -*- coding: utf-8 -*-
#  @Time    : 2019/7/3 20:00
#  @Author  : Kimani
# script downloads movies from goojara.ch
# usage: python3 goojara.py <url>
# url is the link to the movie page on goojara.ch
# example: python3 goojara.py https://www.goojara.ch/0Ez1Zz
import sys
import requests
from bs4 import BeautifulSoup
import os
import re
import subprocess
import time
import shutil
from urllib.parse import urlparse

def download_movie(url):
    # get the movie page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # get the title of the movie
    title = soup.find('h1').text
    # get the download links
    links = soup.find_all('a', class_='dowload')
    # get the download link with the highest quality
    link = links[-1]['href']
    # get the filename of the movie
    filename = os.path.basename(urlparse(link).path)
    # download the movie
    print('Downloading', title)
    with open(filename, 'wb') as f:
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')
        if total_length is None:
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write('\r[%s%s]' % ('=' * done, ' ' * (50 - done)))
                sys.stdout.flush()
    print('\nDownload complete')
    # extract the movie
    print('Extracting', title)
    subprocess.run(['unrar', 'e', filename])
    print('Extraction complete')
    # remove the rar file
    os.remove(filename)
    # get the name of the extracted folder
    folder = re.sub(r'\.rar$', '', filename)
    # get the name of the movie file
    movie = os.listdir(folder)[0]
    # rename the movie file
    shutil.move(os.path.join(folder, movie), title + '.mkv')
    # remove the extracted folder
    shutil.rmtree(folder)
    print('Downloaded', title)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python3 goojara.py <url>')
        sys.exit(1)
    url = sys.argv[1]
    download_movie(url)
#the script downloads movies from goojara.ch. It takes the URL of the movie page as an argument and downloads the movie to the current directory. The script uses the requests module to download the movie page, the BeautifulSoup module to parse the HTML content of the page, and the unrar command to extract the movie file. The script also displays a progress bar while downloading the movie and extracts the movie to a folder before renaming the movie file and removing the folder.    

