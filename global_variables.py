import pygame
import sys
from random import randint
import math

# Pygame windows settings
pygame.init()
SCREEN = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
CLOCK = pygame.Clock()
AMBIENT_COLOR = (0, 0, 10)
pygame.display.set_caption("Apotrop")

# Pygame mouse cursor settings
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

# Display surface settings
display = pygame.Surface((320, 320))
display.set_colorkey(AMBIENT_COLOR)
map_rotate = 0
display_height = 0

# Display for surface settings
display_fog = pygame.Surface((320, 320), pygame.SRCALPHA)

# Player movement settings
player_position = [0, 0]
player_speed = 0.1

# Graphics loading
player = pygame.image.load('assets/index.svg').convert_alpha()
zombie = pygame.image.load('assets/index-zombie.svg').convert_alpha()
weapon = pygame.image.load('assets/index2.svg').convert_alpha()

# Graphics scaling
player_scaled = pygame.transform.smoothscale(pygame.transform.rotate(player, 180), (16, 16))
zombie_scaled = pygame.transform.smoothscale(zombie, (16, 16))
weapon_scaled = pygame.transform.smoothscale(pygame.transform.rotate(weapon, 180), (16, 16))

class DeltaTime:
    def __init__(self):
        self.value = 0

    def update(self):
        self.value = CLOCK.tick(144)
        return self.value


delta_time = DeltaTime()

class Collisions:
    pass