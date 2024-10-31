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
GOALS: Eat all the enemies
RULES: You have to get a powerup to eat enemies
FEEDBACK: If you collide with an enemy before eating a powerup you die
FREEDOM: Move around inside the game space

What sentence does your game make? 

When the player collides with an enemy the enemy bounces off

'''
# created a game class to instantiate later
# it will have all the necessary parts to run the game
# the game class is created to organize the elements needed to create a gam

class Game: 
    # Set up everything the game needs right when it starts, like the screen, clock, and a flag for pillars
    def __init__(self):
        # Start up Pygame
        pg.init()
        # Set up the display size
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        # Give the window a title
        pg.display.set_caption("Logan's Game")
        # Make a clock so we can control the framerate
        self.clock = pg.time.Clock()
        # Keeps track if the game is running
        self.running = True
        # Flag to decide if pillars should be created
        self.create_pillars = True

    # Load any needed data for the game, like images and maps
    def load_data(self):
        # Path to the main game folder
        self.game_folder = path.dirname(__file__)
        # Folder where images are stored
        self.img_folder = path.join(self.game_folder, 'images')
        # Load up the map file
        self.map = Map(path.join(self.game_folder, 'level1.txt'))

    # Start a new game, setting up the map, player, enemies, etc.
    def new(self):
        # Load in our game data (like the map)
        self.load_data()
        # Print map data for debugging (see what’s in the map)
        print(self.map.data)
        # Groups to keep track of different types of game objects
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()

        # Go through each row in the map file
        for row, tiles in enumerate(self.map.data):
            # Print row number for debugging
            print(row)
            # Go through each tile in that row
            for col, tile in enumerate(tiles):
                # Print column number for debugging
                print(col)
                # If we find a wall, add it at this spot
                if tile == '1':
                    Wall(self, col, row)
                # If there's an enemy mob, add it here
                if tile == 'M':
                    Mob(self, col, row)
                # If we find the player start position, place the player here
                if tile == 'P':
                    self.player = Player(self, col, row)

    # Actually run the game
    def run(self):
        # Set the game to a running state
        self.running = True
        # Main game loop
        while self.running:
            # Keep track of time between frames (delta time)
            self.dt = self.clock.tick(FPS) / 1000
            # Check for input
            self.events()
            # Update all objects
            self.update()
            # Draw everything on screen
            self.draw()

    # Quit the game and close Pygame
    def quit(self):
        # Close Pygame
        pg.quit()
        # Close out the game entirely
        sys.exit()

    # Check for events like closing the game window
    def events(self):
        # Go through all events
        for event in pg.event.get():
            # If the user clicks the close button, stop the game
            if event.type == pg.QUIT:
                self.running = False

    # Update all game objects and check for game-over conditions
    def update(self):
        # Update all sprites (like player, enemies, etc.)
        self.all_sprites.update()
        # If player health is zero or less, end the game
        if self.player.health <= 0:
            self.running = False

    # Draw text to the screen (like for displaying time, score, etc.)
    def draw_text(self, surface, text, size, color, x, y):
        # Find an arial font
        font_name = pg.font.match_font('arial')
        # Set up the font size and color
        font = pg.font.Font(font_name, size)
        # Render the text to a surface
        text_surface = font.render(text, True, color)
        # Get a rectangle for the text
        text_rect = text_surface.get_rect()
        # Position it in the middle of the top of the specified location
        text_rect.midtop = (x, y)
        # Draw the text surface on the screen
        surface.blit(text_surface, text_rect)

    # Draw all game graphics to the screen
    def draw(self):
        # Fill the screen with a color (white)
        self.screen.fill(WHITE)
        # Draw all sprites to the screen
        self.all_sprites.draw(self.screen)
        # Draw the timer at a specific spot
        self.draw_text(self.screen, str(pg.time.get_ticks()), 24, WHITE, WIDTH / 30, HEIGHT / 30)
        # Update the display with new graphics
        pg.display.flip()

    # Pause the game until a key is pressed
    def wait_for_key(self):
        # Flag to stay in this loop until a key is pressed
        waiting = True
        while waiting:
            # Keep the framerate steady while waiting
            self.clock.tick(FPS)
            # Go through each event while waiting
            for event in pg.event.get():
                # If user quits, stop waiting and quit the game
                if event.type == pg.QUIT:
                    waiting = False
                    self.quit()
                # If any key is released, stop waiting
                if event.type == pg.KEYUP:
                    waiting = False

# Make a game object and run the game
if __name__ == "__main__":
    # Create an instance of the Game class
    g = Game()
    # Set up the game elements
    g.new()
    # Run the game loop
    g.run()