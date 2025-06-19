#Build base del maze game
import sys

from presenter import colisiones
from model import personaje,muros,laberinto,boton
import pygame

class View:
    pass

if __name__ == '__main__':
    pygame.init()

    WIDTH = 900 #Ancho
    HEIGHT = 650 #Alto
    screen = pygame.display.set_mode([WIDTH, HEIGHT]) #Display de la pantalla
    timer = pygame.time.Clock() #Timer para que se ejecute
    fps = 60
    pygame.display.set_caption('MAZEGAME')
    gameIcon = pygame.image.load('../sprites/fotojuego.jpg')
    pygame.display.set_icon(gameIcon)


    #Sprites de player
    player = personaje.Personaje(50,50)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)

    #Sprite grupo paredes y puertas
    paredes = pygame.sprite.Group()
    door_azul = pygame.sprite.Group()

    #Sprite de botones
    botones_azules = pygame.sprite.Group()
    bot1 = boton.Boton() #Botones
    botones_azules.add(bot1) #Añadir al grupo sprites


    #Añadir puertas azules
    puerta = muros.Puerta(laberinto.puerta1[0], laberinto.puerta1[1], laberinto.puerta1[2], laberinto.puerta1[3])
    paredes.add(puerta)
    door_azul.add(puerta)




    for x, y, w, h in laberinto.paredes_lista_1: #Dibujo del laberinto seleccionado
        pared = muros.Muro(x, y, w, h)
        paredes.add(pared)
        all_sprites_list.add(pared)


    #Bucle del funcionamiento del juego
    run = True
    while run:
        timer.tick(fps)
        screen.fill('black')

        #Event que va leyendo los eventos y hace un bucle de los eventos dentro de bucle del juego
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Boton de salida
                run = False
                sys.exit()

        colisiones.Colisiones.move(player,paredes,WIDTH,HEIGHT) #Llama a la funcion Personaje.move
        colisiones.Colisiones.pulsar(player,botones_azules,door_azul)


        if botones_azules.has(bot1) == 0:
            paredes.remove(puerta)

        all_sprites_list.update() #Update la lista de sprites
        all_sprites_list.draw(screen) #Dibuja Sprites
        botones_azules.draw(screen) #Dibuja boton
        door_azul.draw(screen) #Dibuja boton
        pygame.display.flip() #Reset pantalla por cada tick

    pygame.quit()