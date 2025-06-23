import pygame
from pygame.sprite import Sprite
Azul = (0,0,255)




class BotonAzul(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10 * 2, 10 * 2), pygame.SRCALPHA)  # Superficie con canal alfa (transparente)
        pygame.draw.circle(self.image, Azul, (10, 10), 10)  # Dibujar el círculo
        self.rect = self.image.get_rect(center=(100,580))


class BotonVerde(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10 * 2, 10 * 2), pygame.SRCALPHA)  # Superficie con canal alfa (transparente)
        pygame.draw.circle(self.image, (0,255,0), (10, 10), 10)  # Dibujar el círculo
        self.rect = self.image.get_rect(center=(550,580))

class Meta(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(topleft=(x, y))