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
                mant = pygame.key.get_pressed()
                if tecla == pygame.K_LEFT:
                        while mant[K_LEFT] == True:
                                self.rect.x -= 5





