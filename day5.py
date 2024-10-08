#This file was created by logan azzolina

#This cde was created by Chatgpt

import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invaders")

# Load player image
player_img = pygame.image.load('player.png')
player_x = screen_width / 2 - 32
player_y = screen_height - 100
player_x_change = 0

# Load enemy image
enemy_img = pygame.image.load('enemy.png')
enemy_x = random.randint(0, screen_width - 64)
enemy_y = random.randint(50, 150)
enemy_x_change = 2
enemy_y_change = 40

# Load bullet image
bullet_img = pygame.image.load('bullet.png')
bullet_x = 0
bullet_y = player_y
bullet_y_change = -4
bullet_state = "ready"  # "ready" means you can't see the bullet on the screen, "fire" means the bullet is moving

# Function to draw the player on the screen
def player(x, y):
    screen.blit(player_img, (x, y))

# Function to draw the enemy on the screen
def enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Function to fire the bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

# Function to check for collision between the bullet and the enemy
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2) ** 0.5
    return distance < 27

# Main game loop
running = True
while running:
    # Fill the screen with a black background
    screen.fill(black)

    # Check for events such as key presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If a keystroke is pressed, check whether it's left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -3
            if event.key == pygame.K_RIGHT:
                player_x_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Update player position
    player_x += player_x_change

    # Keep the player within screen bounds
    if player_x <= 0:
        player_x = 0
    elif player_x >= screen_width - 64:
        player_x = screen_width - 64

    # Update enemy position
    enemy_x += enemy_x_change
    if enemy_x <= 0:
        enemy_x_change = 2
        enemy_y += enemy_y_change
    elif enemy_x >= screen_width - 64:
        enemy_x_change = -2
        enemy_y += enemy_y_change

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y += bullet_y_change

    # Reset bullet when it moves out of the screen
    if bullet_y <= 0:
        bullet_y = player_y
        bullet_state = "ready"

    # Check for collision
    collision = is_collision(enemy_x, enemy_y, bullet_x, bullet_y)
    if collision:
        bullet_y = player_y
        bullet_state = "ready"
        enemy_x = random.randint(0, screen_width - 64)
        enemy_y = random.randint(50, 150)

    # Draw the player and enemy
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
Steps to Run the Game:
