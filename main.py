import pygame
from classes import Player, Level1, Level3, Level3

BACKGROUND = (0, 154, 255)

# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Create an 1280x720 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the title of the window
pygame.display.set_caption('Worlds hardest game')


# Handle movement of enemies
def enemy_handler(x, y):
    global enemy_list
    for enemy in enemy_list:
        enemy.changespeed(x, y)


# Call this function so the Pygame library can initialize itself
pygame.init()

# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

levels = [Level1(), Level3(), Level3()]
current_level = 0

# Create the player paddle object
player = Player(50, 50)
player.walls = levels[current_level].wall_list
player.enemies = levels[current_level].enemy_list

all_sprite_list.add(player)

clock = pygame.time.Clock()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, -3)
            elif event.key == pygame.K_s:
                player.changespeed(0, 3)

            elif event.key == pygame.K_LEFT:
                enemy_handler(-3, 0)
            elif event.key == pygame.K_RIGHT:
                enemy_handler(3, 0)
            elif event.key == pygame.K_UP:
                enemy_handler(0, -3)
            elif event.key == pygame.K_DOWN:
                enemy_handler(0, 3)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.changespeed(3, 0)
            elif event.key == pygame.K_d:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_w:
                player.changespeed(0, 3)
            elif event.key == pygame.K_s:
                player.changespeed(0, -3)


            elif event.key == pygame.K_LEFT:
                enemy_handler(3, 0)
            elif event.key == pygame.K_RIGHT:
                enemy_handler(-3, 0)
            elif event.key == pygame.K_UP:
                enemy_handler(0, 3)
            elif event.key == pygame.K_DOWN:
                enemy_handler(0, -3)

    all_sprite_list.update()

    screen.fill(BACKGROUND)

    all_sprite_list.draw(screen)

    levels[current_level].draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
