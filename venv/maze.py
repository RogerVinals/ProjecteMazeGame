#Build base del maze game
import sys

from personaje import Personaje
from laberinto import laberintos
import pygame

pygame.init()

WIDTH = 600 #Ancho
HEIGHT =650 #Alto
screen = pygame.display.set_mode([WIDTH, HEIGHT]) #Display de la pantalla
timer = pygame.time.Clock() #Timer para que se ejecute
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = laberintos
pygame.display.set_caption('maze game')
gameIcon = pygame.image.load('../sprites/fotojuego.jpg')
pygame.display.set_icon(gameIcon)

#Posicion Inicial
player = Personaje((0,255,0),10,10)
player.rect.x = 100
player.rect.y = 100
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

#Dinujo del nivel
run = True
while run:
    timer.tick(fps)
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Boton de salida
            run = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            Personaje.move(player,event.key)

    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()

pygame.quit()