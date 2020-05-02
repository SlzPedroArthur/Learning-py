#from the archive, follow each link, find the image in that linked page, 
#and download the image.

#1.Download files => urllib;
#2.Parse HTML => Beautifulsoup;
import os
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup

base_url = 'https://apod.nasa.gov/apod/archivepix.html'
download_directory = 'apod-pictures'
content = urllib.request.urlopen(base_url).read()
cont = 0
for link in BeautifulSoup(content, 'lxml').findAll('a'):
   
   if (cont<4):
      cont += 1
      continue
      
   print('Link:', link)
   href = urljoin(base_url, link['href'])

   contentIn = urllib.request.urlopen(href).read()
   
   for img in BeautifulSoup(contentIn, 'lxml').finAll('img'):
      img_href = urljoin(href, img['src'])
      print('Downloading image: ', img_href)
      img_name = img_href.split('/')[-1] #[-1] means take the last one
      urllib.request.urlretrieve(img_href, os.path.join(download_directory, img_name))