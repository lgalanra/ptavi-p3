#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys
import json
import urllib.request

class KaraokeLocal():
    def __init__(self):
        parser = make_parser()
        myHandler = SmallSMILHandler()
        parser.setContentHandler(myHandler)
        parser.parse(open(sys.argv[1]))
        self.datos = myHandler.get_tags()

    def __str__(self):
        texto = ''
        for dicc in self.datos:
            linea = ''
            linea = linea + dicc['name']
            for tag in dicc:
                if tag != 'name' and dicc[tag] != '':
                    linea = linea + '\t' + tag + '="' + dicc[tag] + '"'
                    texto = texto + linea
        return(texto)

    def to_json(self):
        json.dump(datos, open('karaoke.json', 'w'))

    def do_local(self):
        for dicc in datos:
            linea = ''
            linea = linea + dicc['name']
            for tag in dicc:
                if tag == 'src':
                    if dicc[tag].startswith('http://'):
                        recorte = dicc[tag].split('/')[-1]
                        urllib.request.urlretrieve(dicc[tag], recorte)
                        dicc[tag] = recorte
                if tag != 'name' and dicc[tag] != '':
                    linea = linea + '\t' + tag + '="' + dicc[tag] + '"'

if __name__ == "__main__":
    try:
        luis = KaraokeLocal()
        parser = make_parser()
        myHandler = SmallSMILHandler()
        parser.setContentHandler(myHandler)
        parser.parse(open(sys.argv[1]))

    except ValueError:
        sys.exit('Usage: python3 karaoke.py file.smil')
