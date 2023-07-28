import pygame, random
pygame.init()

#PUT FUNCTIONS HERE
def reset():
    global brick_rect, wall_top_rect, wall_bottom_rect
    brick_rect.y = 250
    wall_top_rect.x = WIDTH//2
    wall_top_rect.y = -(WALL_HEIGHT//2)
    wall_bottom_rect.x = WIDTH//2
    wall_bottom_rect.y = wall_top_rect.y + WALL_HEIGHT + gap

def reset_walls():
    global wall_top_rect, wall_bottom_rect
    wall_top_rect.x = WIDTH
    wall_bottom_rect.x = WIDTH
    wall_top_rect.y = random.randint(-10, 4)*5
    wall_bottom_rect.y = wall_top_rect.y + WALL_HEIGHT + (random.randint(25, 35)*5)

# GLOBAL VARIABLES
ORANGE = (255, 165, 0)
BLACK = (0, 0, 0)
BLUE = (75, 90, 238)

# Select the font to use, size, bold, italics
font = pygame.font.SysFont('Calibri', 25, True, False)

# Screen dimensions
WIDTH = 600 
HEIGHT = 400

#setup screen
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode(size)

#setup brick
brick = pygame.sprite.Sprite()
brick.image = pygame.image.load("images/brick.png")
brick_rect = brick.image.get_rect()
brick_rect.x = 90
brick_rect.y = 250

#setup walls
wall_top = pygame.sprite.Sprite()
wall_bottom = pygame.sprite.Sprite()
wall_top.image = pygame.image.load("images/wall-top.png")
WALL_HEIGHT = wall_top.image.get_rect().height
wall_bottom.image = pygame.image.load("images/wall-bottom.png")
wall_bottom_height = wall_bottom.image.get_rect().height
wall_bottom_width = wall_bottom.image.get_rect().width
gap = WIDTH//4
wall_top_rect = wall_top.image.get_rect()
wall_top_rect.x = WIDTH//2
wall_top_rect.y = -(WALL_HEIGHT//2)
wall_bottom_rect = wall_bottom.image.get_rect()
wall_bottom_rect.x = WIDTH//2
wall_bottom_rect.y = wall_top_rect.y + WALL_HEIGHT + gap

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#setup score
score = 0


done = False

#MAIN GAME LOOP
while not done:
    for event in pygame.event.get():
        #manage quit click
        if event.type == pygame.QUIT:
            done = True
        #manage mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            brick_rect.y = brick_rect.y - 30

    #UPDATE ALL THE SPRITES
    brick_rect.y = brick_rect.y + 1
    wall_top_rect.x = wall_top_rect.x - 1
    wall_bottom_rect.x = wall_bottom_rect.x - 1

    #CHECK FOR COLLISIONS
    is_hit = brick_rect.colliderect(wall_top_rect) or brick_rect.colliderect(wall_bottom_rect)

    if is_hit:
        reset()
    if brick_rect.y > (HEIGHT - brick_rect.height):
        reset()
    if wall_top_rect.x < 0:
        score = score + 1
        reset_walls()

    #DISPLAY EVERYTHING
    screen.fill(BLUE)
    screen.blit(brick.image, [brick_rect.x, brick_rect.y])
    screen.blit(wall_top.image, [wall_top_rect.x, wall_top_rect.y])
    screen.blit(wall_bottom.image, [wall_bottom_rect.x, wall_bottom_rect.y])

    # Add score text
    text = font.render(str(score), True, ORANGE)
    screen.blit(text, (500, 30))

    pygame.display.flip()

    # Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
