#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.milista = []

    def startElement(self, name, attrs):
        if name == 'root-layout':
            dicc = {}
            dicc['width'] = attrs.get('width', '')
            dicc['height'] = attrs.get('height', '')
            dicc['background-color'] = attrs.get('background-color','')
            self.milista.append(dicc)
        elif name == 'region':
            dicc = {}
            dicc['id'] = attrs.get('id','')
            dicc['top'] = attrs.get('top','')
            dicc['bottom'] = attrs.get('bottom','')
            dicc['left'] = attrs.get('left','')
            dicc['right'] = attrs.get('right','')
            self.milista.append(dicc)
        elif name == 'img':
            dicc = {}
            dicc['src'] = attrs.get('src','')
            dicc['region'] = attrs.get('region','')
            dicc['begin'] = attrs.get('begin','')
            dicc['dur'] = attrs.get('dur','')
            self.milista.append(dicc)
        elif name == 'audio':
            dicc = {}
            dicc['src'] = attrs.get('src','')
            dicc['begin'] = attrs.get('begin','')
            dicc['dur'] = attrs.get('dur','')
            self.milista.append(dicc)
        elif name == 'textstream':
            dicc = {}
            dicc['src'] = attrs.get('src','')
            dicc['region'] = attrs.get('region','')
            self.milista.append(dicc)

    def get_tags(lista):
        pass

if __name__ == "__main__":
    pass
