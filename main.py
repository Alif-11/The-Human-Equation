import pygame

# initialize the library
pygame.init()

# set the size of the game screen
screen = pygame.display.set_mode([700,700])
# set up clock, to help with the FPS of the game
clock = pygame.time.Clock()
running = True

# used for physics independent of framerate
dt = 0
# get the player position
player_position = pygame.Vector2(screen.get_width()/2-40, screen.get_height()/2-40)
enemy_position = pygame.Vector2(screen.get_width()/4, screen.get_height()/4)

while running:
  for event in pygame.event.get():
    # if the user clicked the window X button
    if event.type == pygame.QUIT:
      # break out of the for loop, in other words, end the game
      running = False
  # wipe screen, to remove objects from last frame.
  screen.fill("black")

  ####################
  # Code for your game
  # draw player
  pygame.draw.circle(screen,"white", player_position, 20)
  # draw enemy
  pygame.draw.circle(screen,"red",enemy_position,15)
  # draw enemy eye
  pygame.draw.circle(screen,"black",enemy_position,5)
  pressed_keys = pygame.key.get_pressed()
  if pressed_keys[pygame.K_UP]:
    player_position.y -= 150 * dt
  if pressed_keys[pygame.K_DOWN]:
    player_position.y += 150 * dt
  if pressed_keys[pygame.K_LEFT]:
    player_position.x -= 150 * dt
  if pressed_keys[pygame.K_RIGHT]:
    player_position.x += 150 * dt

  # End of game code--
  ####################
  # display your game on the window screen
  pygame.display.flip()
  # limit game frames per second to 30
  dt = clock.tick(30) / 1000



# the game is done!
pygame.quit()