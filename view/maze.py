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
    door_verde = pygame.sprite.Group()

    #Sprite de botones
    botones_azules = pygame.sprite.Group()
    bot1 = boton.BotonAzul() #Botone azul
    botones_azules.add(bot1) #Añadir al grupo sprites
    botones_verde = pygame.sprite.Group()
    bot2 = boton.BotonVerde() #Boton Verde
    botones_verde.add(bot2)


    #Añadir puertas azules
    puerta_azul = muros.PuertaAzul(laberinto.puerta1[0], laberinto.puerta1[1], laberinto.puerta1[2], laberinto.puerta1[3])
    puerta_verde = muros.PuertaVerde(laberinto.puerta2[0], laberinto.puerta2[1], laberinto.puerta2[2], laberinto.puerta2[3])
    paredes.add(puerta_azul)
    door_azul.add(puerta_azul)
    paredes.add(puerta_verde)
    door_verde.add(puerta_verde)

    #Añadir meta de laberinto
    meta = boton.Meta(laberinto.meta[0],laberinto.meta[1],laberinto.meta[2],laberinto.meta[3])
    metas = pygame.sprite.Group()
    metas.add(meta)




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
        colisiones.Colisiones.pulsar(player,botones_verde,door_verde)
        colisiones.Colisiones.victoria(player,metas)


        if botones_azules.has(bot1) == 0:
            paredes.remove(puerta_azul)
        if botones_verde.has(bot2) == 0:
            paredes.remove(puerta_verde)
        if metas.has(meta) == 0:
            sys.exit()

        all_sprites_list.update() #Update la lista de sprites
        all_sprites_list.draw(screen) #Dibuja Sprites
        botones_azules.draw(screen) #Dibuja boton azul
        botones_verde.draw(screen) #Dibuja boton verde
        door_azul.draw(screen) #Dibuja puerta azul
        door_verde.draw(screen)#Dibuja puerta verde
        metas.draw(screen)
        pygame.display.flip() #Reset pantalla por cada tick

    pygame.quit()