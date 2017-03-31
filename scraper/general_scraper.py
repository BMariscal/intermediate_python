import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base_url= 'https://apod.nasa.gov/apod/archivepix.html'
download_directory= "apod_pictures"
# What it does:
# so long as the page still has a link to visit. The script is going to visit the link,
# it's going to extract any new links we havent seen before, it's going
# to download images in that page and it's going to keep going until it doesn't
#  have any more links left to visit
to_visit = set((base_url,))
visited = set()

while to_visit:
    # pick a link to visit.
    # visit the link.
    current_page = to_visit.pop()
    print("visiting:", current_page)
    visited.add(current_page)
    content = urllib.request.urlopen(current_page).read()

    # Extract any new links from that page.
    for link in BeautifulSoup(content, "lxml").findAll("a"):
        absolute_link = urljoin(current_page, link["href"])
        if absolute_link not in visited:
            to_visit.add(absolute_link)
        else:
            print("Already visited:", absolute_link)
    # Download any images on the page.
    for img in BeautifulSoup(content, "lxml").findAll("img"):
        img_href = urljoin(current_page, img["src"])
        print("Downloading image:", img_href)
        img_name =  img_href.split("/")[-1]
        urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))
