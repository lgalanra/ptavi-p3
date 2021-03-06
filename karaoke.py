#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler
import sys
import json
import urllib.request


class KaraokeLocal():
    def __init__(self):
        self.resultante = ''
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
                    linea = linea + '\t' + tag + '="' + dicc[tag] + '"\t'
            texto = texto + linea + '\n'
        return(texto)

    def to_json(self, resultante):
        if resultante is "":
            json.dump(self.datos, open(nombreFichero, 'w'),
                      sort_keys=True, indent=4, separators=(',', ': '))
        else:
            json.dump(self.datos, open("local.json", 'w'),
                      sort_keys=True, indent=4, separators=(',', ': '))

    def do_local(self):
        myHandler = SmallSMILHandler()
        for dicc in self.datos:
            linea = ''
            linea = linea + dicc['name']
            for tag in dicc:
                if tag == 'src':
                    if dicc[tag].startswith('http://'):
                        recorte = dicc[tag].split('/')[-1]
                        urllib.request.urlretrieve(dicc[tag], recorte)
                        dicc[tag] = recorte
                if tag != 'name' and dicc[tag] != '':
                    linea = linea + '\t' + tag + '="' + dicc[tag] + '"\t'

if __name__ == "__main__":
    try:
        luis = KaraokeLocal()
        parser = make_parser()
        myHandler = SmallSMILHandler()
        parser.setContentHandler(myHandler)
        parser.parse(open(sys.argv[1]))
        n = str(sys.argv[1])
        nombreFichero = n.split(".")[0]+".json"
    except ValueError:
        sys.exit('Usage: python3 karaoke.py file.smil')

print(luis)
luis.to_json("")
luis.do_local()
luis.to_json("local.json")
print(luis)
