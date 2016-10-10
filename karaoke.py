#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys

if __name__ == "__main__":
    try:
        file = open(sys.argv[1])

    except ValueError:
        sys.exit('Usage: python3 karaoke.py file.smil')

archivo = file.read()

parser = make_parser()
myHandler = SmallSMILHandler()
parser.setContentHandler(myHandler)
parser.parse(archivo)
myHandler.get_tags()
