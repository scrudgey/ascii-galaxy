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

api = twitter.Api(consumer_key=cred.consumer_key,
                  consumer_secret=cred.consumer_secret,
                  access_token_key=cred.access_token,
                  access_token_secret=cred.access_token_secret)
# print(api.VerifyCredentials())

def test():
  print generate_image()

def post_ascii_galaxy():
  """Generate and then post an ASCII galaxy."""
  img = generate_image()
  post_image(img)

def generate_image():
  # TODO: get random image from folder
  path =  'imgs/' + random.choice(os.listdir('imgs'))
  img = ascii.handle_image_conversion(path)
  return img

def post_image(img):
  status = api.PostUpdate(img)
  print(status.text)

if __name__=='__main__':
  post_ascii_galaxy()
