import pygame
from pygame import sprite, K_LEFT
from pygame.sprite import Sprite


class Personaje(pygame.sprite.Sprite): #clase jugador
        def __init__(self,color,width,height):
                super().__init__()
                self.image = pygame.Surface([50,50])
                self.image.fill((0,255,0))
                pygame.draw.rect(self.image,color,pygame.Rect(0,0,50,50))
                self.rect = self.image.get_rect()

        def move(self,tecla):
                if tecla == pygame.K_LEFT:
                        self.rect.x -= 2
                if tecla == pygame.K_RIGHT:
                        self.rect.x += 2
                if tecla == pygame.K_UP:
                        self.rect.y -= 2
                if tecla == pygame.K_DOWN:
                        self.rect.y += 2





