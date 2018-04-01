# -*- coding: utf-8 -*-
"""
ASCII Galaxy
Generate and post ASCII images of galaxies.
"""
import os
import random
import twitter

import cred
import ascii
import wiki_scrape

api = twitter.Api(consumer_key=cred.consumer_key,
                  consumer_secret=cred.consumer_secret,
                  access_token_key=cred.access_token,
                  access_token_secret=cred.access_token_secret)
# print(api.VerifyCredentials())

def test_file(name):
  image_names = os.listdir('imgs')
  for image_name in image_names:
    if name in image_name:
      path =  'imgs/' + image_name
      img = ascii.handle_image_conversion(path)
      print path
      print img

def test():
  print generate_image()

def post_ascii_galaxy():
  """Generate and then post an ASCII galaxy."""
  img = generate_image()
  post_image(img)

def generate_image():
  path =  'imgs/' + random.choice(os.listdir('imgs'))
  img = ascii.handle_image_conversion(path)
  return img

def post_image(img):
  status = api.PostUpdate(img)
  print(status.text)

if __name__=='__main__':
  print 'posting galaxy...'
  post_ascii_galaxy()
