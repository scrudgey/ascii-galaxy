import wikipedia
import re
import urllib
import os
import logging
logging.basicConfig(filename='urls.log',level=logging.INFO)

BULLSHIT = [u'age: https://upload.wikimedia.org/wikipedia/commons/a/a4/Charles_Messier.jpg',
            u'https://upload.wikimedia.org/wikipedia/en/f/fd/Portal-puzzle.svg',
            u'https://upload.wikimedia.org/wikipedia/commons/8/83/Celestia.png',
            u'https://upload.wikimedia.org/wikipedia/commons/9/93/Infrared_color_magnitude_diagram_of_Messier_79.png']

def fix_file():
  titles, names = get_names()
  for i, name in enumerate(names):
    print '{}: {}'.format(i, name)
  choice = raw_input("Re-download which image? ")
  index = int(choice)
  download_image(titles[index], names[index])

def download_messier_images():
  titles, names = get_names()
  for title, name in zip(titles, names):
    print title
    download_image(title, name)

def get_names():
  title_hook = re.compile(r'title="(.+)"')
  name_hook = re.compile(r'<a.+?>(.+?)<')
  titles = []
  names = []
  for line in open('messier.txt', 'r'):
    match = title_hook.search(line)
    if match:
      titles.append(match.group(1))
      names.append(name_hook.search(line).group(1))
  return titles, names

def get_url(page_title):
  page = wikipedia.page(page_title)
  index = 0
  img_url = page.images[index]
  while img_url in BULLSHIT or 'map' in img_url or img_url[-4:] == '.svg':
    index += 1
    img_url = page.images[index]
  return img_url

def download_image(page_title, filename):
  img_url = get_url(page_title)
  print ' - Main Image: {}'.format(img_url)
  logging.info('{}: {}'.format(page_title, img_url))
  extension = img_url.split('/')[-1].split('.')[-1]
  download_path = 'imgs/' + filename + '.' + extension
  if os.path.exists(download_path):
    os.remove(download_path)
  urllib.urlretrieve(img_url, download_path)

if __name__=='__main__':
  download_messier_images()
