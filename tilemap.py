#This file was created by Logan Azzolina 

import pygame as pg
from settings import *


class Map:
    def __init__(self, filename): # init filename 
        self.data = [] # makes list for self data
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data) 
        self.width = self.tilewidth * TILESIZE #set width 
        self.height = self.tileheight * TILESIZE # set height 