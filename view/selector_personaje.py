import pygame
import sys

def seleccionar_personaje():
    pygame.init()
    WIDTH, HEIGHT = 900, 650
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Seleccionar Personaje")

    font = pygame.font.SysFont("Arial", 40)
    small_font = pygame.font.SysFont("Arial", 28)

    personajes = [
        ("MonoBazuca", "../sprites/pngwing.com.png"),
        ("Oficinista", "../sprites/man.png"),
        ("Pirata", "../sprites/manpirata.png")
    ]
    index = 0

    while True:
        screen.fill((25, 25, 25))
        texto = font.render("Selecciona tu personaje", True, (200, 200, 255))
        screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, 60))

        # Imagen del personaje
        nombre, ruta_imagen = personajes[index]
        imagen = pygame.image.load(ruta_imagen)
        imagen = pygame.transform.scale(imagen, (100, 100))
        screen.blit(imagen, (WIDTH // 2 - 50, 200))

        # Nombre
        nombre_texto = small_font.render(nombre, True, (255, 255, 0))
        screen.blit(nombre_texto, (WIDTH // 2 - nombre_texto.get_width() // 2, 320))

        # Flechas
        flecha_izq = small_font.render("<", True, (255, 255, 255))
        flecha_der = small_font.render(">", True, (255, 255, 255))
        screen.blit(flecha_izq, (WIDTH // 2 - 120, 240))
        screen.blit(flecha_der, (WIDTH // 2 + 100, 240))

        continuar_text = small_font.render("Presiona ENTER para continuar", True, (180, 180, 180))
        screen.blit(continuar_text, (WIDTH // 2 - continuar_text.get_width() // 2, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    index = (index - 1) % len(personajes)
                elif event.key == pygame.K_RIGHT:
                    index = (index + 1) % len(personajes)
                elif event.key == pygame.K_RETURN:
                    return index
