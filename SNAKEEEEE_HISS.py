import pygame
import random

pygame.init()

# Farger
skjermbakgrunn = (213, 50, 80)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

# Skjerm størrelse
width = 600
height = 400

# Lage skjerm/display
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Størrelse til snake/block
block_size = 10

# font stil som viser score
font_style = pygame.font.SysFont(None, 30)

# definere en funksjon som viser scoren
def display_score(score):
    score_text = font_style.render("Score: " + str(score), True, black)
    dis.blit(score_text, [0, 0])

# definere main spill loop
def game_loop():
    # definere start posisjon a snake
    x = width / 2
    y = height / 2
    

    # definere change i posisjon til snake
    x_change = 0
    y_change = 0

    # definere posisjon til mat/ det som blir spist av snake
    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    # definer score
    score = 0

    #set farte til slange
    speed = 10

    # start game loop
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0

        # Update posisjon til snake
        x += x_change
        y += y_change

        # sjekk om snake treffer veggen/wall
        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True

        # fyll vindu med hvit farge
        dis.fill(skjermbakgrunn) 

        # tegne mat
        pygame.draw.rect(dis, green, [food_x, food_y, block_size, block_size])

        # tegne snake
        pygame.draw.rect(dis, black, [x, y, block_size, block_size])

        # sjekk dersom snake spiser opp mat
        if x == food_x and y == food_y:
            score += 1            

            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0



        # vis/display scoren
        display_score(score)

        # Update scoren
        pygame.display.update()

        # Set farten til snake
        pygame.time.Clock().tick(20)

    # slutt games
    pygame.quit()
    quit()

# start game
game_loop()
