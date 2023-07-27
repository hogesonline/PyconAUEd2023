import pygame
pygame.init()

# GLOBAL VARIABLES
COLOR = (255, 100, 98)
BLACK = (0, 0, 0)

# Screen dimensions
WIDTH = 600
HEIGHT = 400

#setup screen
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)

#setup brick
brick = pygame.sprite.Sprite()
brick.image.load("images/brick.png")
brick.rect = player.image.get_rect()
brick.x = 90
brick.y = 250

#setup walls
wall_top = pygame.sprite.Sprite()
wall_bottom = pygame.sprite.Sprite()
wall_top.image.load("images/wall_top.png")
wall_bottom.image.load("images/wall_bottom.png")
gap = 150
wall_top.x = 300
wall_top.y = 0
wall_bottom.x = 300
wall_bottom.y = wall_top.height + gap

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    

    screen.fill(BLACK)
    screen.blit(brick.image, [brick.x, brick.y])
    screen.blit(wall_top.image, [wall_top.x, wall_top.y])
    screen.blit(wall_bottom.image, [wall_bottom.x, wall_bottom.y])

    pygame.display.flip()



