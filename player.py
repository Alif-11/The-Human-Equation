##
# Extension of the sprite file, to draw the player object

#
##

import pygame
from sprite import Sprite
from user_input import is_key_pressed

class Player(Sprite): # extending Sprite class
  def __init__(self, image, x, y):
    super().__init__(image, x, y)
    self.movement_speed = 2
  

  def update(self):
    if is_key_pressed(pygame.K_UP):
      self.y -= self.movement_speed
    if is_key_pressed(pygame.K_DOWN):
      self.y += self.movement_speed
    if is_key_pressed(pygame.K_RIGHT):
      self.x += self.movement_speed
    if is_key_pressed(pygame.K_LEFT):
      self.x -= self.movement_speed
    