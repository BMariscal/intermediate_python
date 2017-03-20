#From the apod archive, follow each link, find the image in that linked page, and download the image.

# Concepts:
#1. Downloading stuff => urllib
#2. Parsing stuff out of HTML => BeautifulSoup


#Download the index page
import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base_url= 'https://apod.nasa.gov/apod/archivepix.html'
download_directory= "apod_pictures"
content = urllib.request.urlopen(base_url).read()


#For each link on the index page:
for link in BeautifulSoup(content, "lxml").findAll("a"):
    print("Following link:", link)
    href = urljoin(base_url, link["href"])
#  Follow the link and pull down the image on the linked page
    content = urllib.request.urlopen(href).read()
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(href, img["src"])
        print("Downloading image:", img_href)
        img_name = img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
