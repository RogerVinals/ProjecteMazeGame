#Build base del maze game
import sys

import laberinto
from personaje import Personaje
from muros import Muro
import pygame


pygame.init()

WIDTH = 900 #Ancho
HEIGHT = 650 #Alto
screen = pygame.display.set_mode([WIDTH, HEIGHT]) #Display de la pantalla
timer = pygame.time.Clock() #Timer para que se ejecute
fps = 60
pygame.display.set_caption('MAZEGAME')
gameIcon = pygame.image.load('../sprites/fotojuego.jpg')
pygame.display.set_icon(gameIcon)

#Sprites
player = Personaje(50,50)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)
paredes = pygame.sprite.Group()

for x, y, w, h in laberinto.paredes_lista_1: #Dibujo del laberinto seleccionado
    pared = Muro(x, y, w, h)
    paredes.add(pared)
    all_sprites_list.add(pared)


#Bucle del funcionamiento del juego
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')

    #Event que va leyendo los eventos y hace un bucle de los eventos dentro de bucle del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Boton de salida
            run = False
            sys.exit()

    player.move(paredes,WIDTH,HEIGHT) #Llama a la funcion Personaje.move

    all_sprites_list.update() #Update la lista de sprites
    all_sprites_list.draw(screen) #Dibuja Sprites
    pygame.display.flip() #Reset pantalla por cada tick

pygame.quit()