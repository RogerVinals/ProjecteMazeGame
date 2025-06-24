import pygame
import random

psiz = 40  # Tamaño de celda

def generar_laberinto_backtracking(ancho_pix, alto_pix,nivel):
    columnas = ancho_pix // psiz
    filas = alto_pix // psiz

    visitado = [[False for _ in range(columnas)] for _ in range(filas)]
    paredes = []

    def vecinos_validos(x, y):
        dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        random.shuffle(dirs)
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < columnas and 0 <= ny < filas and not visitado[ny][nx]:
                yield nx, ny, dx, dy

    def remover_paredes(x1, y1, x2, y2):
        px = min(x1, x2)
        py = min(y1, y2)
        if x1 == x2:
            # horizontal
            paredes.remove((x1 * psiz, py * psiz + psiz, psiz, 1))
        elif y1 == y2:
            # vertical
            paredes.remove((px * psiz + psiz, y1 * psiz, 1, psiz))

    def crear_muros_iniciales():
        for y in range(filas):
            for x in range(columnas):
                if x < columnas - 1:
                    paredes.append((x * psiz + psiz, y * psiz, 1, psiz))  # vertical
                if y < filas - 1:
                    paredes.append((x * psiz, y * psiz + psiz, psiz, 1))  # horizontal

    def backtrack(x, y):
        visitado[y][x] = True
        for nx, ny, dx, dy in vecinos_validos(x, y):
            if not visitado[ny][nx]:
                remover_paredes(x, y, nx, ny)
                backtrack(nx, ny)

    # bordes
    borde_grosor = 5
    paredes_borde = [
        (0, 0, ancho_pix, borde_grosor),                      # top
        (0, 0, borde_grosor, alto_pix),                       # left
        (0, alto_pix - borde_grosor, ancho_pix, borde_grosor),  # bottom
        (ancho_pix - borde_grosor, 0, borde_grosor, alto_pix)   # right
    ]


    crear_muros_iniciales()
    backtrack(0, 0)  # empieza desde esquina superior izquierda

    # Si el nivel es fácil, eliminamos más paredes aleatorias
    if nivel == 0:  # fácil
        random.shuffle(paredes)
        extra = int(len(paredes) * 0.25)  # elimina 25%
        paredes = paredes[extra:]
    elif nivel == 1:  # intermedio
        random.shuffle(paredes)
        extra = int(len(paredes) * 0.1)  # elimina 10%
        paredes = paredes[extra:]

    # nivel == 2 (difícil): no se elimina nada
    # Asegura que el mono (inicio) tenga espacio libre
    espacios_inicio = [
        (0, 0), (1, 0), (2, 0),
        (0, 1), (1, 1), (2, 1),
        (0, 2), (1, 2), (2, 2)
    ]
    for cx, cy in espacios_inicio:
        px = cx * psiz
        py = cy * psiz

        # Remover pared vertical derecha
        try:
            paredes.remove((px + psiz, py, 1, psiz))
        except ValueError:
            pass

        # Remover pared horizontal inferior
        try:
            paredes.remove((px, py + psiz, psiz, 1))
        except ValueError:
            pass

    return paredes + paredes_borde

# Coordenadas de una puerta fija (puedes cambiarla o eliminarla si quieres puertas dinámicas)
puerta1 = (100, 100, 10, 10)
