#from lib2to3.pygram import python_grammar_no_print_and_exec_statement

import pygame
from pygame import sprite, K_LEFT
from pygame.sprite import Sprite
#from model.laberinto import generar_laberinto



import pygame

class Colisiones:
    @staticmethod
    def move(player, paredes, ancho, alto):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]: dx = -player.velocidad
        if keys[pygame.K_RIGHT]: dx = player.velocidad
        if keys[pygame.K_UP]: dy = -player.velocidad
        if keys[pygame.K_DOWN]: dy = player.velocidad

        # Movimiento horizontal y colisiones
        player.rect.x += dx
        if pygame.sprite.spritecollideany(player, paredes) or player.rect.left < 0 or player.rect.right > ancho:
            player.rect.x -= dx

        # Movimiento vertical y colisiones
        player.rect.y += dy
        if pygame.sprite.spritecollideany(player, paredes) or player.rect.bottom > alto or player.rect.top < 0:
            player.rect.y -= dy

    @staticmethod
    def pulsar(player, botones, puertas):
        if pygame.sprite.spritecollideany(player, botones):
            botones.empty()
            puertas.empty()




