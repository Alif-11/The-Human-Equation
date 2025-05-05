##
# Class to handle sprite work in the game

#
##

import pygame
loaded = dict()
sprites = []

class Sprite:

  def __init__(self, image, x, y):
    """
    Initialize Sprite Object
    """
    if image in loaded: # sprite already exists
      self.image = loaded[image] # get the value associated with the key image
    else:
      # load the image
      self.image = pygame.image.load(image)
      loaded[image] = self.image # create new mapping between key image, and a value
                                 # of the already loaded image
    self.x = x
    self.y = y
    sprites.append(self)
  
  def delete(self):
    sprites.remove(self)
  
  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))