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

parser = make_parser()
myHandler = SmallSMILHandler()
parser.setContentHandler(myHandler)
parser.parse(file)
datos = myHandler.get_tags()

for dicc in datos:
    linea = ''
    linea = linea + dicc['name']
    for tag in dicc:
        if tag != 'name' and dicc[tag] != '':
            linea = linea + '\t' + tag + '="' + dicc[tag] + '"'
    print(linea)
