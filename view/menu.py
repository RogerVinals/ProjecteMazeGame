import pygame
import sys
from view.selector_personaje import seleccionar_personaje  # Asegúrate de tener este archivo

# Personajes definidos
personajes = ["MonoBazuca", "Oficinista", "Pirata"]

# Esta variable se actualizará al seleccionar personaje
personaje_idx = 0

def menu_principal():
    global personaje_idx
    pygame.init()
    WIDTH, HEIGHT = 900, 650
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MENÚ - MAZEGAME")
    font = pygame.font.SysFont("Arial", 40)
    small_font = pygame.font.SysFont("Arial", 25)

    opciones = ["Iniciar Juego", "Seleccionar Personaje", "Salir"]
    seleccionada = 0

    while True:
        screen.fill((20, 20, 20))

        titulo = font.render("MAZE GAME", True, (200, 200, 255))
        screen.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 60))

        for i, texto in enumerate(opciones):
            color = (255, 255, 255) if i == seleccionada else (180, 180, 180)
            render = font.render(texto, True, color)
            screen.blit(render, (WIDTH // 2 - render.get_width() // 2, 200 + i * 60))

        # Mostrar personaje actual
        nombre_actual = personajes[personaje_idx]
        p_text = small_font.render(f"Personaje seleccionado: {nombre_actual}", True, (255, 255, 0))
        screen.blit(p_text, (WIDTH // 2 - p_text.get_width() // 2, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    seleccionada = (seleccionada + 1) % len(opciones)
                elif event.key == pygame.K_UP:
                    seleccionada = (seleccionada - 1) % len(opciones)
                elif event.key == pygame.K_RETURN:
                    if opciones[seleccionada] == "Iniciar Juego":
                        return personaje_idx
                    elif opciones[seleccionada] == "Seleccionar Personaje":
                        personaje_idx = seleccionar_personaje()
                    elif opciones[seleccionada] == "Salir":
                        sys.exit()

def seleccionar_nivel():
    pygame.init()
    WIDTH, HEIGHT = 900, 650
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Seleccionar Nivel")

    font = pygame.font.SysFont("Arial", 40)
    opciones = ["Nivel Fácil", "Nivel Intermedio", "Nivel Difícil", "Modo Carrera"]
    seleccion = 0

    while True:
        screen.fill((30, 30, 30))
        titulo = font.render("Selecciona la dificultad", True, (200, 200, 255))
        screen.blit(titulo, (WIDTH // 2 - titulo.get_width() // 2, 100))

        for i, texto in enumerate(opciones):
            color = (255, 255, 255) if i == seleccion else (150, 150, 150)
            render = font.render(texto, True, color)
            screen.blit(render, (WIDTH // 2 - render.get_width() // 2, 200 + i * 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    seleccion = (seleccion + 1) % len(opciones)
                elif event.key == pygame.K_UP:
                    seleccion = (seleccion - 1) % len(opciones)
                elif event.key == pygame.K_RETURN:
                    if opciones[seleccion] == "Modo Carrera":
                        return "carrera"
                    else:
                        return seleccion  # 0: fácil, 1: medio, 2: difícil
