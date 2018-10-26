#!/usr/bin/python
import getopt
import sys
from PIL import Image

def usage():
  print('Usage: monika_decode.py [-v] [FILE]')
  sys.exit(2)

def main(argv):
  if len(argv) == 0:
    usage()
  verbose = False
  input = ''
  for arg in argv:
    if arg == '-v':
      verbose = True
    else:
      input = arg
  if len(input) == 0:
    usage()
  image = Image.open(input)
  width, height = image.size
  
  i = 0
  value = 0
  bits = ''
  text = ''
  for y in range(height):
    for x in range(width):
      pixel = image.getpixel((x, y))
      mean = (pixel[0] + pixel[1] + pixel[2]) / 3
      bit = 1 if mean >= 128 else 0
      bits += str(bit)
      value = value | (bit << (7 - i))
      i += 1
      if i >= 8:
        text += chr(value)
        value = 0
        i = 0
    bits += '\n'
  if verbose:
    print('Input image: {}x{}'.format(width, height))
    print('Bits:')
    print(bits)
    print('Result string:')
  print(text)

if __name__ == '__main__':
  main(sys.argv[1:])
