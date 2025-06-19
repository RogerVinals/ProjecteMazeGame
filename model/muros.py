import pygame

#Colores
Negro = (0,0,0)
Blanco = (255,255,255)
Azul = (0,0,255)
Marron = (158,70,36)

class Muro(pygame.sprite.Sprite):
    def __init__(self,x,y,ancho,alto):
        super().__init__()
        self.image = pygame.Surface((ancho,alto))
        self.image.fill(Marron)
        self.rect = self.image.get_rect(topleft=(x,y))


class Puerta(pygame.sprite.Sprite):
    def __init__(self,x,y,ancho,alto):
        super().__init__()
        self.image = pygame.Surface((ancho,alto))
        self.image.fill(Azul)


if __name__ == '__main__':
    pass