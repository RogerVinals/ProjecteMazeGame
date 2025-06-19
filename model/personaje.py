import pygame
from pygame.sprite import Sprite




class Personaje(pygame.sprite.Sprite): #clase jugador
        def __init__(self,width,height):
                super().__init__()
                self.image = pygame.transform.scale(pygame.image.load("../sprites/pngwing.com.png"), (width, height)).convert_alpha()
                self.rect = self.image.get_rect(topleft=(width,height))
                self.rect.x = 0
                self.rect.y = 0
                self.velocidad = 5
if __name__ == '__main__':
    pass

