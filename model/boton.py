import pygame
import random
import os

Azul = (0, 0, 255)

#class Boton(pygame.sprite.Sprite):
    #def __init__(self):
        #super().__init__()
        #self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        #pygame.draw.circle(self.image, Azul, (10, 10), 10)
        #self.rect = self.image.get_rect(center=(100, 580))


class Llave(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ruta = os.path.join("..", "sprites", "llave_puerta.png")
        self.image = pygame.image.load(ruta).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))  # Ajusta el tamaño si es necesario
        self.rect = self.image.get_rect()

    def colocar_en_posicion_libre(self, paredes, ancho_total, alto_total):
        intentos = 0
        while intentos < 100:
            x = random.randint(50, ancho_total - 50)
            y = random.randint(50, alto_total - 50)
            self.rect.topleft = (x, y)
            if not pygame.sprite.spritecollideany(self, paredes):
                return
            intentos += 1
        print("No se encontró una posición válida para la llave.")

