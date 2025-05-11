
##
# Contains main game loop

#
##


import pygame
import user_input

# initialize the library
pygame.init()

# Game Name
pygame.display.set_caption("A Human's Equation")

# set the size of the game screen
clear_color = (200,200,200)
screen = pygame.display.set_mode((1280,780))
screen.fill(clear_color)

    # display changes
pygame.display.flip()
# is game running?
running = True

sprite_sheet = pygame.image.load("images/Sprout Lands - Sprites - Basic pack/Characters/Basic Charakter Spritesheet.png").convert_alpha()

def get_image(spritesheet, width, height):
  image = pygame.Surface((width, height)).convert_alpha() # creates a new image
  image.blit(spritesheet, (0,0), (0, 0, width, height)) # takes the sprite sheet,
  # takes the 0,0 coordinate, takes the square of width width and height height
  # and draws it on the image surface.

  return image

bunny_character = get_image(sprite_sheet, 44, 44)

# game loop
while running:

  # loop through every event occurring
  for game_event in pygame.event.get():
    if game_event.type == pygame.QUIT:
      running = False
    
    if game_event.type == pygame.KEYDOWN:
      user_input.keys_down.add(game_event.key)

    
    if game_event.type == pygame.KEYUP:
      user_input.keys_down.remove(game_event.key)

    
    # draw on the screen
    screen.fill(clear_color)

    # draw bunny, at position 0,0
    screen.blit(bunny_character, (0,0))

    #screen.blit(sprite_sheet, (0,0))

    # display changes
    pygame.display.update()

pygame.quit()
