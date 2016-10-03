#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.milista = []

    def startElement(self, name, attrs):
        if name == 'root-layout':
            rootdicc = {}
            dicc['width'] = attrs.get('width', '')
            dicc['height'] = attrs.get('height', '')
            dicc['background-color'] = attrs.get('background-color','')
            milista.append(rootdicc)
        elif name == 'region':
            namedicc = {}
            dicc['id'] = attrs.get('id','')
            dicc['top'] = attrs.get('top','')
            dicc['bottom'] = attrs.get('bottom','')
            dicc['left'] = attrs.get('left','')
            dicc['right'] = attrs.get('right','')
            milista.append(namedicc)
        elif name == 'img':
            imgdicc = {}
            dicc['src'] = attrs.get('src','')
            dicc['region'] = attrs.get('region','')
            dicc['begin'] = attrs.get('begin','')
            dicc['dur'] = attrs.get('dur','')
            milista.append(imgdicc)
        elif name == 'audio':
            audiodicc = {}
            dicc['src'] = attrs.get('src','')
            dicc['begin'] = attrs.get('begin','')
            dicc['dur'] = attrs.get('dur','')
            milista.append(audiodicc)
        elif name == 'textstream':
            textdicc = {}
            dicc['src'] = attrs.get('src','')
            dicc['region'] = attrs.get('region','')
            milista.append(textdicc)

if __name__ == "__main__":
    pass
