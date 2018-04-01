# -*- coding: utf-8 -*-
import PIL
from PIL import Image
from PIL import ImageOps
import sys
import ipdb

CHARS = [ u'．', u'｀', u'：', u'ｏ', u'Ｏ', u'８', u'＊', u'Ｈ', u'＃', u'＠', u'Ｗ']
ALPHABET = u'ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ０１２３４５６７８９'

def convert_text_to_monospace(text):
    output = u''
    for char in text:
        if char in '0123456789':
            index = ord(char) - ord('0')
            start_index = 26
        else:
            index = ord(char) - ord('A')
            start_index = 0
        output = output + ALPHABET[index + start_index]
    return output

def map_pixels_to_ascii_chars(image, bin_width=25):
    """Maps each pixel to an ascii char based on the range
    in which it lies.

    0-255 is divided into 11 bins of 25 pixels each.
    """
    pixels = list(image.getdata())
    ascii = [CHARS[value / bin_width] for value in pixels]
    return "".join(ascii)

def adjust_image_levels(image):
    width, height = image.size
    minval = min(image.getdata())
    maxval = max(image.getdata())
    for i in range(0, width):
        for j in range(0, height):
            pixel=image.getpixel((i,j))
            new_val = (pixel-minval)*(255/maxval)
            image.putpixel((i,j),new_val)

def convert_image_to_ascii(image, new_width=11):
    image = ImageOps.fit(image, (new_width, new_width), method=PIL.Image.LANCZOS)
    image = image.convert('L')
    adjust_image_levels(image)
    # ipdb.set_trace()

    # TODO: rescale values?
    ascii = map_pixels_to_ascii_chars(image)
    lines = [ascii[index: index + new_width] for index in
            xrange(0, len(ascii), new_width)]
    return "\n".join(lines)

def add_title(ascii, path):
    """Each row is 11 characters wide."""
    names = path.split('/')
    filename = names[-1].split('.')[0]
    output = ascii[:-11]
    line = ascii[-11:]
    title = convert_text_to_monospace(filename)

    start_index = int(5 - int((len(title)-1))/2.0)
    if start_index < 0:
        raise Exception('title too long! {}'.format(start_index))

    for char in line[0:start_index]:
        output += char
    for char in title:
        output += char
    for char in line[start_index+len(title):]:
        output += char
    return output

def handle_image_conversion(path, width=11):
    image = None
    try:
        image = Image.open(path)
    except Exception, e:
        print "Can't open {}".format(path)
        print e
        return
    ascii = convert_image_to_ascii(image, new_width=width)
    ascii = add_title(ascii, path)
    return ascii

if __name__=='__main__':
    handle_image_conversion(sys.argv[1])
