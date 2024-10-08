# This file was created by Logan Azzolina


#import all necessary moduals and librarys
import pygame as pg 
from settings import * 
from sprites import *
#created a game class to instantiate later
#It will have all necessary parts to run the game
class Game:
    def _init_(self):
       pg.init()
       pg.mixer.init()
       self.screen = pg.display.set_mode((WIDTH,HEIGHT))
       pg.display.set_caption("Logan' Game")
       self.running = True 
def new(self):
    self.all_sprites = pg.sprite.Group()
    self.player

    def run(self):
        while self.running:
            for event in pg.event.get():
              if event.type == pg. QUIT:
                 self.running = False
            self.screen.fill((0,0,0))
            pg.display.flip()
        pg.quit()


if __name__=="__main__":
   g = Game()
   g.run()
   