import wikipedia
import re
import urllib
# import ipdb

import logging
logging.basicConfig(filename='urls.log')

bullshit = [u'https://upload.wikimedia.org/wikipedia/en/4/4a/Commons-logo.svg',
            u'https://upload.wikimedia.org/wikipedia/en/4/48/Folder_Hexagonal_Icon.svg',
            u'https://upload.wikimedia.org/wikipedia/en/f/fd/Portal-puzzle.svg',
            u'https://upload.wikimedia.org/wikipedia/commons/8/83/Celestia.png',
            u'https://upload.wikimedia.org/wikipedia/commons/8/89/Symbol_book_class2.svg']

title_hook = re.compile(r'title="(.+)"')
name_hook = re.compile(r'<a.+?>(.+?)<')

titles = []
names = []
for line in open('messier.txt', 'r'):
  match = title_hook.search(line)
  if match:
    titles.append(match.group(1))
    names.append(name_hook.search(line).group(1))

for title, name in zip(titles, names):
  print title
  page = wikipedia.page(title)
  index = 0
  img_url = page.images[index]
  while img_url in bullshit:
    index += 1
    img_url = page.images[index]
  print ' - Main Image: {}'.format(img_url)
  logging.info('{}: {}'.format(title, img_url))
  image_name = img_url.split('/')[-1]
  extension = image_name.split('.')[-1]
  download_path = 'imgs/' + name + '.' + extension
  urllib.urlretrieve(img_irl, download_path)
