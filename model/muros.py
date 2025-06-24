import pygame
import os
#Colores que se van a usar.
Negro = (0,0,0)
Blanco = (255,255,255)
Azul = (0,0,255)
Marron = (158,70,36)
Verde = (0, 255, 0)




class Muro(pygame.sprite.Sprite):
    def __init__(self,x,y,ancho,alto):
        super().__init__()
        self.image = pygame.Surface((ancho,alto))
        self.image.fill(Marron)  #Muro lo rellena de marron
        self.rect = self.image.get_rect(topleft=(x,y))

class Salida(pygame.sprite.Sprite):
    def __init__(self, x, y, ancho, alto):
        super().__init__()
        self.image = pygame.Surface((ancho, alto))
        self.image.fill(Verde)  # Verde
        self.rect = self.image.get_rect(topleft=(x, y))


class Puerta(pygame.sprite.Sprite):
    def __init__(self,x,y,ancho,alto):
        super().__init__()
        self.image = pygame.Surface((ancho,alto))
        self.image.fill(Azul)
        self.rect = self.image.get_rect(topleft=(x, y))

class PuertaJuego(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        ruta_base = os.path.dirname(__file__)
        ruta_sprites = os.path.join(ruta_base, "..", "sprites")

        # Carga y escala las imágenes
        self.imagen_cerrada = pygame.image.load(os.path.join(ruta_sprites, "puerta_cerrada.png")).convert_alpha()
        self.imagen_cerrada = pygame.transform.scale(self.imagen_cerrada, (30, 50))

        self.imagen_abierta = pygame.image.load(os.path.join(ruta_sprites, "puerta_abierta.png")).convert_alpha()
        self.imagen_abierta = pygame.transform.scale(self.imagen_abierta, (30, 50))

        self.image = self.imagen_cerrada
        self.rect = self.image.get_rect(topleft=(x, y))
        self.abierta = False

    def abrir(self):
        self.abierta = True
        self.image = self.imagen_abierta
if __name__ == '__main__':
    pass