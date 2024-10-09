# This file was created by Logan Azzolina

#anything anything 

# IMPORT ALL NECESSARY MODULES AND LIBRARIES
import pygame as pg

from settings import *
from sprites import *
from tilemap import *
from os import path 
from random import randint
'''
GOALS : eat all the enemies 
RULES : you have to get powerup to eat enemies
FEEDBACK: If you collide with enemy before hitting powerup you die
FREEDOM: MOve around inside game spae

What setance does your game make? (mario video)

When the player collides with enemy the enemy bounces off


'''

# created a game class to instantiate later
# it will have all the necessary parts to run the game
#the game class is created to orginize the elements needed to create a game
#this inlcudes the game clock which allows us to set the framerate
class Game:
    # init initializes all the neccesary components for the game including video and sound 
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Logan' Game")
        self.clock = pg.time.Clock()
        self.running = True
        # self creates player block, creates the all_sprites group so that we can batch, update and render. defines properties that can be seen in the game system. 
        #self creates a player block and defines classes 
    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.map = Map(path.join(self. game_folder, 'level1.txt'))
    def new(self):
        self.load_data()
        print(self.map.data)
        #following steps instanciate all the items that will be in the game system.
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 50,50)
        # instantiated a mob
        self.mob = Mob(self, 100,100)
        self.wall1 = Wall(self, 100,100)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.mob)
        self.all_sprites.add(self.wall1)
        #creating for loop for how many you want of something.
        # makes new mobs and walls using a for loop
        for i in range(6):
            print(i*TILESIZE)
            w = Wall(self, i*TILESIZE, 100)
            self.all_sprites.add(w)
        #takes map.data and parses it usign enumerate so that we can assign x and y values to object intsnaces.
        for row, tiles in enumerate(self.map.date):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'p':
                    Player(self, col, row)
                if tile == 'm':
                    Mob(self, col, row)
                if tile == 'C':
                    Coin(self,col,row)

    # using self.running as a boolean to continue running the game.-------- does the actions like draw sprites.
    def run(self):
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
        # input 
    #Looks for any event, and specifically looks for closing the game with 'x'.
    def events(self):
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

        # pg.quit()
        # process
    # constantly checking for updates for the group of sprites. 
    def update(self):
        self.all_sprites.update()
        # output
    def draw_text(self, surface,text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surface.blit(text_surface, text_rect)
    # drawing out whats on the screen like the fill color. 
    def draw(self):
        self.screen.fill(WHITE)
        self.draw_text(self.screen, str(self.dt*1000), 24, BLACK, WIDTH/2, HEIGHT/2)
        self.all_sprites.draw(self.screen,"Coins collected " + str(self.player.coins), 24, WHITE, WIDTH /2, HEIGHT/24)
        pg.display.flip()

# if the name of the file is main then run!
#checks file name and creates a game object
if __name__ == "__main__":
    g = Game()
    # create all game elements with the new method (not function)
    g.new()
    #run the game
    g.run()

        