# #This file was created by logan azzolina

import pygame as pg
from pygame.sprite import Sprite
from settings import *
import random

vec = pg.math.Vector2

class Player(Sprite): ## This class defines the player character, managing their movement, jumping, and interaction with the environment.
    # initializes the player with the game reference and starting pos
    def __init__(self, game, x, y): ## Here, we set up the player’s position, visual appearance, initial movement properties, and health.
        self.game = game  # save the game reference
        self.groups = game.all_sprites  # put player in all_sprites group
        Sprite.__init__(self, self.groups)  # initiate the sprite
        
        # create the player image square
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()  # get the rectangle area of image
        self.image.fill(RED)  # make player red
        
        # set up the starting position and movement vectors
        self.pos = vec(x * TILESIZE, y * TILESIZE)
        self.vel = vec(0, 0)  # velocity starts at 0
        self.acc = vec(0, 0)  # acceleration starts at 0
        self.speed = 5  # speed to control movement
        self.jumping = False  # player not jumping yet
        self.jump_power = 1  # how high the player can jump
        # self.coins = 0  # coins start at 0
        self.health = 10  # starting health

    # check keys pressed for movement
    def get_keys(self): ## This method checks which keys are being pressed (WASD for movement and space for jumping) and updates the player's movement.
        keys = pg.key.get_pressed()  # get key states
        if keys[pg.K_w]:  # if W, move up
            self.vel.y -= self.speed
        if keys[pg.K_a]:  # if A, move left
            self.vel.x -= self.speed
        if keys[pg.K_d]:  # if D, move right
            self.vel.x += self.speed
        if keys[pg.K_SPACE]:  # if SPACE, jump
            self.jump()

    # define jumping class
    def jump(self): ## In this block, we check if the player is grounded and then apply the physics needed for jumping.
        self.rect.y += 2  # move down a bit to check collision
        hits = pg.sprite.spritecollide(self, self.game.all_walls, False)  # check if we hit ground
        self.rect.y -= 2  # move back
        if hits and not self.jumping:  # if touching ground and not already jumping
            self.jumping = True  # start the jump
            self.vel.y = -self.jump_power  # jump up
            print("trying to jump")

    # handle collision with walls in x and y directions
    def collide_with_walls(self, dir):  ## This part checks for collisions with walls in either the x or y direction and adjusts the player’s position accordingly.
        if dir == 'x':  # checking x direction collision
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vel.x > 0:  # moving right
                    self.pos.x = hits[0].rect.left - TILESIZE
                if self.vel.x < 0:  # moving left
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0  # stop horizontal movement
                self.rect.x = self.pos.x
        if dir == 'y':  # checking y direction collision
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vel.y > 0:  # falling down
                    self.pos.y = hits[0].rect.top - TILESIZE
                    self.jumping = False  # stop jumping
                if self.vel.y < 0:  # moving up
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0  # stop vertical movement
                self.rect.y = self.pos.y

    # check collision with any sprite in the group
    def collide_with_stuff(self, group, kill):  ## Here, we check if the player collides with any other objects (like barrels), and if so, handle the interaction (like quitting the game).
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Barrel":  # check if hit a Barrel
                print("i hit a Barrel...")
                self.game.quit()
    def collide_with_dk(self):
        hits = pg.sprite.spritecollide(self, self.game.all_dk, False)
        if hits:
            print("You win!")  # Replace with actual win logic
            self.game.running = False  # Stop the game or trigger a win screen

    # update player position and handle friction
    def update(self):   ## In this method, we update the player's position based on velocity and gravity, and check for any wall collisions that might change their position.
        self.acc = vec(0, GRAVITY)  # apply gravity
        self.get_keys()  # check keys
        self.acc.x += self.vel.x * FRICTION  # add friction
        self.vel += self.acc  # update velocity with acceleration
        if abs(self.vel.x) < 0.1:  # stop any tiny movement
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc  # update position
        self.rect.x = self.pos.x  # update rect x
        self.collide_with_walls('x')  # check x collision
        self.rect.y = self.pos.y  # update rect y
        self.collide_with_walls('y')  # check y collision
        self.collide_with_stuff(self.game.all_mobs, False)  # check mob collision
        self.collide_with_dk()

class Mob(Sprite):
    # init mob, with game ref and position
    def __init__(self, game, x, y):
        self.game = game  # store game reference
        self.groups = game.all_sprites, game.all_mobs  # put mob in all_sprites and all_mobs
        Sprite.__init__(self, self.groups)  # init sprite
        
        # create mob image
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(GREEN)  # make it green
        self.rect.x = x * TILESIZE  # set x pos
        self.rect.y = y * TILESIZE  # set y pos
        self.speed = 10  # speed of mob

    # update mob position
    def update(self):
        self.rect.x += self.speed  # move in x
        hits = pg.sprite.spritecollide(self, self.game.all_walls, False)  # check wall collision
        if hits:
            self.speed *= -1  # reverse direction
            self.rect.y += TILESIZE * 2  # move down
#setup barrel to have similar physics to player allowing for gravity 
class Barrel(Sprite):       
    # init mob, with game ref and position
    def __init__(self, game, x, y):
        self.game = game  # store game reference
        self.groups = game.all_sprites, game.all_mobs  # put mob in all_sprites and all_mobs
        Sprite.__init__(self, self.groups)  # init sprite
        
        # create mob image
        self.image = pg.Surface((TILESIZE, TILESIZE))   
        self.rect = self.image.get_rect()   # Get the rectangle for collision and positioning
        self.image.fill(GREEN)  # make it green
        self.pos = vec(x*TILESIZE, y*TILESIZE)  # Position the barrel in the game space
        self.vel = vec(0,0) # Initial velocity (stationary at first)
        self.acc = vec(0,0) # Acceleration is zero initially
        self.speed = -1  # Set the initial speed for horizontal movement

    def collide_with_walls(self, dir):
        if dir == 'x':  # checking x direction collision
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)    #set hits for if else statement 
            if hits:
                if self.vel.x > 0:  # moving right 
                    self.pos.x = hits[0].rect.left - TILESIZE   # Stop at the left edge of the wall
                    self.speed *= -1   # if hit wall from left switch direction by reversing speed
                if self.vel.x < 0:  # moving left
                    self.pos.x = hits[0].rect.right
                    self.speed *= -1    # if hit wall from right switch firection by reversing speed
                self.vel.x = 0  # stop horizontal movement
                self.rect.x = self.pos.x
        if dir == 'y':  # checking y direction collision
            hits = pg.sprite.spritecollide(self, self.game.all_walls, False)
            if hits:
                if self.vel.y > 0:  # falling down
                    self.pos.y = hits[0].rect.top - TILESIZE
                   
                if self.vel.y < 0:  # moving up
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0  # stop vertical movement
                self.rect.y = self.pos.y

    
        
    # update mob position
    def update(self):
        self.acc = vec(self.speed, GRAVITY)  # Set acceleration with gravity
        self.acc.x += self.vel.x * FRICTION  # Apply friction to horizontal movement
        self.vel += self.acc  # Update velocity with acceleration
        if abs(self.vel.x) < .1:  # If velocity is very small, stop moving horizontally
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc  # Update position based on velocity and acceleration
        self.rect.x = self.pos.x  # Update horizontal position
        self.collide_with_walls('x')  # Check for horizontal collisions
        self.rect.y = self.pos.y  # Update vertical position
        self.collide_with_walls('y')  # Check for vertical collisions
        

class Wall(Sprite):
    # init wall with game ref and position
    def __init__(self, game, x, y):
        self.game = game  # store game ref
        self.groups = game.all_sprites, game.all_walls  # add to all_sprites and all_walls
        Sprite.__init__(self, self.groups)  # init sprite
        
        # create wall image
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.rect = self.image.get_rect()
        self.image.fill(BLUE)  # make wall blue
        self.rect.x = x * TILESIZE  # set x pos
        self.rect.y = y * TILESIZE  # set y pos

    # walls don’t need to update
        def update(self):
            pass  
class DonkeyKong(Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self.groups = game.all_sprites, game.all_dk
        Sprite.__init__(self, self.groups)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)  # Make Donkey Kong yellow
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

        def update(self):
            pass 
