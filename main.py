import pygame,sys
from player import Player

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Game")

running = True

#Initiating player
player = Player(0, 0, 32, 32, (255, 0, 0), .075, 0, 0)

while running:
    player.x += player.move_x
    player.y += player.move_y

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #Checking player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.move_y = -player.move_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.move_y = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player.move_y = player.move_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player.move_y = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.move_x -= player.move_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player.move_x = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move_x += player.move_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.move_x = 0


    screen.fill((0, 255, 0))

    #Draw player
    pygame.draw.rect(screen, player.colour, (player.x, player.y, player.width, player.height), 0)
    pygame.display.update()


