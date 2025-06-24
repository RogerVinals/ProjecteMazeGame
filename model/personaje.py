import pygame
import random
import os
from pygame.sprite import Sprite

# Lista de rutas de los sprites
sprites_personajes = [
    "../sprites/pngwing.com.png",
    "../sprites/man.png",  # Puedes cambiar esto por otro personaje más adelante
    "../sprites/manpirata.png"
]

class Personaje(pygame.sprite.Sprite):
    def __init__(self, width, height, idx_sprite=0):
        super().__init__()
        # Elegir sprite según índice. Si el índice es inválido, usar el primero.
        try:
            ruta_sprite = sprites_personajes[idx_sprite]
        except IndexError:
            ruta_sprite = sprites_personajes[0]

        # Cargar imagen escalada
        self.image = pygame.transform.scale(
            pygame.image.load(ruta_sprite), (width, height)
        ).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20
        self.velocidad = 3

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad=2):
        super().__init__()
        ruta_imagen = os.path.join("..", "sprites", "enemigo_suspenso.png")
        self.image = pygame.image.load(ruta_imagen).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))  # Ajusta tamaño si es necesario
        self.rect = self.image.get_rect(center=(x, y))
        self.velocidad = velocidad
        self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        self.movimiento = pygame.Vector2(0, 0)
        self.definir_direccion()

    def definir_direccion(self):
        direcciones = {
            "arriba": pygame.Vector2(0, -self.velocidad),
            "abajo": pygame.Vector2(0, self.velocidad),
            "izquierda": pygame.Vector2(-self.velocidad, 0),
            "derecha": pygame.Vector2(self.velocidad, 0)
        }
        self.movimiento = direcciones[self.direccion]

    def cambiar_direccion(self):
        opciones = ["arriba", "abajo", "izquierda", "derecha"]
        opciones.remove(self.direccion)
        self.direccion = random.choice(opciones)
        self.definir_direccion()

    def update(self, paredes):
        self.rect.move_ip(self.movimiento)
        if pygame.sprite.spritecollideany(self, paredes):
            self.rect.move_ip(-self.movimiento.x, -self.movimiento.y)
            self.cambiar_direccion()