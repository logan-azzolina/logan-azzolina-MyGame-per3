# # This file was created by Logan Azzolina

# IMPORT ALL NECESSARY MODULES AND LIBRARIES
import pygame as pg
from settings import *
from sprites_sidescroller import *
# from sprites import *
from tilemap import *
from os import path
import sys
from random import randint
'''
GOALS: Move freely throughout the game space with the objective of making it to the top of the game space while 
avoiding being hit by the barrels so that you do not die. 
RULES: If you are hit by the barrel you will lose the game/ die. If you hit a powerup you will have a short immunity from the barrels. 
FEEDBACK: If you get hit by a barrel without having eaten a powerup you will lose/die. 
FREEDOM: Move around inside the game space freely. 



'''
# created a game class to instantiate later
# it will have all the necessary parts to run the game
# the game class is created to organize the elements needed to create a gam

class Game: 
    # Initializes the game components 
    def __init__(self):
        pg.init()  # initialize pygame
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))  # create the screen
        pg.display.set_caption("Logan's' Game")  # game title

        self.clock = pg.time.Clock()  # set up game clock for framerate
        self.running = True  # flag to keep the game running
        self.create_pillars = True  # another game control flag

    # Load game assets and other data, like images and maps
    def load_data(self):
        self.game_folder = path.dirname(__file__)  # game folder path
        #load high score file
        with open('HS_file', 'w') as files:
            f.write("High score FIle!") #write some text to the file

        print("file created and written succesfully.")

        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.img_folder = path.join(self.game_folder, 'images')  # image folder path
        self.map = Map(path.join(self.game_folder, 'level1.txt'))  # load the map file

    # Sets up a new game, resets the sprites and other things
    def new(self):
        self.load_data()  # loads all data for the game
        print(self.map.data)  # prints map data for debug
        self.all_sprites = pg.sprite.Group()  # group for all sprites
        self.all_walls = pg.sprite.Group()  # group for wall sprites
        self.all_mobs = pg.sprite.Group()  # group for mob spritesddddw
        
        # Loops through the map data to create walls, mobs, player at specified spots
        #setting the code for the level 1 text
        for row, tiles in enumerate(self.map.data):
            print(row)  # prints row for debug
            for col, tile in enumerate(tiles):
                print(col)  # prints col for debug
                if tile == '1':  # if tile is wall
                    Wall(self, col, row)
                if tile == 'M':  # if tile is mob
                    Mob(self, col, row)
                if tile == 'B':  # if tile is Barrel
                    Barrel(self, col, row)
                if tile == 'P':  # if tile is player
                    self.player = Player(self, col, row)

    # main game loop to keep the game going while running is True
    def run(self):
        self.running = True  # start running
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000  # time delta for frame
            # main three things to do anything
            self.events()  # check for player actions
            self.update()  # update game state
            self.draw()  # render everything to the screen

    # quits the game completely
    def quit(self):
        pg.quit()  # quits pygame
        sys.exit()  # exits the system

    # handle all in-game events, checks if the window is closed
    def events(self):
        for event in pg.event.get():  # loop through events
            if self.score > self.highscore:
                self.highscore > self.score
                self.highscore = self.score
                with open('HS_file', 'w') as files:
                    f.write("High score FIle!") #write some text to the file

            if event.type == pg.QUIT:  # if window's closed
                self.running = False  # stop running

    # updates all sprites and checks game over conditions
    def update(self):
        self.all_sprites.update()  # update every sprite in the game
        if self.player.health <= 0:  # if player health reaches zero = game ends 
            self.running = False  # game ends

    # Draws text to the screen
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('arial')  # match font
        font = pg.font.Font(font_name, size)  # set up font and size
        text_surface = font.render(text, True, color)  # render text
        text_rect = text_surface.get_rect()  # get rectangle of text
        text_rect.midtop = (x, y)  # set position of text
        surface.blit(text_surface, text_rect)  # draw text to screen

    # Draws all elements to the screen
    def draw(self):
        self.screen.fill(WHITE)  # fills screen with white
        self.all_sprites.draw(self.screen)  # draw all sprites
        self.draw_text(self.screen, str(pg.time.get_ticks()), 24, WHITE, WIDTH/30, HEIGHT/30)  # display time
        pg.display.flip()  # update the display

    # waits for a key press to continue
    def wait_for_key(self):
        waiting = True  # set waiting flag
        while waiting:
            self.clock.tick(FPS)  # control framerate
            for event in pg.event.get():  # loop through events
                if event.type == pg.QUIT:  # quit game if quit event
                    waiting = False
                    self.quit()
                if event.type == pg.KEYUP:  # if key released
                    waiting = False  # exit wait

# starts the game if this file is run directly
if __name__ == "__main__":
    g = Game()  # create the game object
    g.new()  # initialize the game elements
    g.run()  # start the game loop
    pg.quit
    
