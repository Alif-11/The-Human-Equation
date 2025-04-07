import pygame

# initialize the library
pygame.init()

# set the size of the game screen
screen = pygame.display.set_mode([700,700])
# set up clock, to help with the FPS of the game
clock = pygame.time.Clock()
running = True

# get the player position
player_position = pygame.Vector2(screen.get_width()/2-40, screen.get_height()/2-40)
while running:
  for event in pygame.event.get():
    # if the user clicked the window X button
    if event.type == pygame.QUIT:
      # break out of the for loop, in other words, end the game
      running = False
  # wipe screen, to remove objects from last frame.
  screen.fill("orange")

  ####################
  # Code for your game
  pygame.draw.circle(screen,"gray", player_position, 30)

  # End of game code--
  ####################
  # display your game on the window screen
  pygame.display.flip()
  # limit game frames per second to 30
  clock.tick(30)



# the game is done!
pygame.quit()