import pygame
from pygame import sprite, K_LEFT
from pygame.sprite import Sprite
class Colisiones(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()

    def move(self,paredes,ancho,alto):
        keys = pygame.key.get_pressed()
        dx = dy = 0
        if keys[pygame.K_LEFT]: dx = -self.velocidad
        if keys[pygame.K_RIGHT]: dx = self.velocidad
        if keys[pygame.K_UP]: dy = -self.velocidad
        if keys[pygame.K_DOWN]: dy = self.velocidad

        # Movimiento horizontal y colisiones
        self.rect.x += dx
        if pygame.sprite.spritecollideany(self, paredes) or self.rect.left < 0 or self.rect.right > ancho:
            self.rect.x -= dx

        # Movimiento vertical y colisiones
        self.rect.y += dy
        if pygame.sprite.spritecollideany(self, paredes) or self.rect.bottom > alto or self.rect.top < 0:
           self.rect.y -= dy