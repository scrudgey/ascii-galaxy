# -*- coding: utf-8 -*-
"""
ASCII Galaxy
Generate and post ASCII images of galaxies.
"""
import cred
import twitter
import pickle

api = twitter.Api(consumer_key=cred.consumer_key,
                  consumer_secret=cred.consumer_secret,
                  access_token_key=cred.access_token,
                  access_token_secret=cred.access_token_secret)

def post_ascii_galaxy():
  """Generate and then post an ASCII galaxy."""
  # print(api.VerifyCredentials())
  img = generate_image()
  post_image(img)

def generate_image():
  return pickle.load(open("img.p", "rb"))

def post_image(img):
  status = api.PostUpdate(img)
  print(status.text)

if __name__=='__main__':
  post_ascii_galaxy()
