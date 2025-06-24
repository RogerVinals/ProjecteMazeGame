import sys
import pygame
import tkinter as tk
from tkinter import messagebox
from presenter import colisiones
from model import personaje, muros, laberinto
from model.boton import Llave
from model.muros import PuertaJuego
from view.menu import menu_principal, seleccionar_nivel
import random
import os

class View:
    pass

def reproducir_musica(path, loop=True):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1 if loop else 0)

def main():
    pygame.init()
    pygame.mixer.init()

    WIDTH, HEIGHT = 900, 650
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('MAZEGAME')
    gameIcon = pygame.image.load('../sprites/fotojuego.jpg')
    pygame.display.set_icon(gameIcon)
    timer = pygame.time.Clock()
    fps = 60

    ruta_audio = os.path.join("..", "audio")
    reproducir_musica(os.path.join(ruta_audio, "8bit_weapon.mp3"))

    personaje_idx = menu_principal()
    modo = seleccionar_nivel()
    niveles_tiempo = [90, 60, 45]
    niveles_en_carrera = [0, 1, 2] if modo == "carrera" else [modo]

    def jugar_nivel(nivel_dificultad, personaje_idx):
        reproducir_musica(os.path.join(ruta_audio, "8bit_weapon.mp3"))

        all_sprites_list = pygame.sprite.Group()
        paredes = pygame.sprite.Group()
        enemigos = pygame.sprite.Group()
        llaves = pygame.sprite.Group()

        # Laberinto
        paredes_lista = laberinto.generar_laberinto_backtracking(WIDTH, HEIGHT, nivel_dificultad)
        for x, y, w, h in paredes_lista:
            pared = muros.Muro(x, y, w, h)
            paredes.add(pared)
            all_sprites_list.add(pared)

        # Jugador
        player = personaje.Personaje(30, 30, personaje_idx)
        all_sprites_list.add(player)

        # Llave colocada sin tocar paredes
        llave = Llave()
        llave.colocar_en_posicion_libre(paredes, WIDTH, HEIGHT)
        llaves.add(llave)
        all_sprites_list.add(llave)

        # Puerta colocada al fondo, intentando evitar colisiones
        puerta_final = PuertaJuego(860, 570)  # y = 570 para no chocar con bordes
        intentos = 0
        while pygame.sprite.spritecollideany(puerta_final, paredes) and intentos < 50:
            puerta_final.rect.topleft = (random.randint(700, 850), random.randint(500, 600))
            intentos += 1
        all_sprites_list.add(puerta_final)
        paredes.add(puerta_final)

        # Enemigo solo en difícil
        if nivel_dificultad == 2:
            intentos = 0
            while intentos < 100:
                enemigo = personaje.Enemigo(random.randint(0, WIDTH), random.randint(0, HEIGHT), velocidad=3)
                if not pygame.sprite.spritecollideany(enemigo, paredes):
                    enemigos.add(enemigo)
                    all_sprites_list.add(enemigo)
                    break
                intentos += 1

        tiempo_maximo_segundos = niveles_tiempo[nivel_dificultad]
        inicio_tiempo = pygame.time.get_ticks()
        tiene_llave = False

        while True:
            timer.tick(fps)
            screen.fill('black')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if HEIGHT - 45 <= my <= HEIGHT - 15:
                        if WIDTH // 4 - 100 <= mx <= WIDTH // 4 + 100:
                            return "menu"
                        if 3 * WIDTH // 4 - 100 <= mx <= 3 * WIDTH // 4 + 100:
                            pygame.quit()
                            sys.exit()

            tiempo_actual = pygame.time.get_ticks()
            tiempo_restante = max(0, tiempo_maximo_segundos - (tiempo_actual - inicio_tiempo) // 1000)

            if tiempo_restante == 0:
                reproducir_musica(os.path.join(ruta_audio, "suspender_4_9.mp3"), loop=False)
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("¡Tiempo agotado!", "Has perdido. Se ha acabado el tiempo.")
                return "menu"

            colisiones.Colisiones.move(player, paredes, WIDTH, HEIGHT)

            if nivel_dificultad == 2 and pygame.sprite.spritecollideany(player, enemigos):
                reproducir_musica(os.path.join(ruta_audio, "mario_bros.mp3"), loop=False)
                root = tk.Tk()
                root.withdraw()
                messagebox.showinfo("¡Has perdido!", "El enemigo te ha atrapado.")
                return "menu"

            if not tiene_llave and pygame.sprite.spritecollideany(player, llaves):
                tiene_llave = True
                llave.kill()
                puerta_final.abrir()
                paredes.remove(puerta_final)

            if pygame.sprite.collide_rect(player, puerta_final) and tiene_llave:
                reproducir_musica(os.path.join(ruta_audio, "komiku_win.mp3"), loop=False)
                return "siguiente"

            for sprite in all_sprites_list:
                if isinstance(sprite, personaje.Enemigo):
                    sprite.update(paredes)
                else:
                    sprite.update()

            all_sprites_list.draw(screen)

            font_timer = pygame.font.SysFont("Arial", 28)
            texto_tiempo = font_timer.render(f"Tiempo restante: {tiempo_restante}s", True, (255, 255, 0))
            screen.blit(texto_tiempo, (WIDTH // 2 - texto_tiempo.get_width() // 2, 10))

            boton_font = pygame.font.SysFont("Arial", 25)
            menu_text = boton_font.render("Volver al Menú", True, (255, 255, 255))
            salir_text = boton_font.render("Salir del Juego", True, (255, 255, 255))
            screen.blit(menu_text, (WIDTH // 4 - menu_text.get_width() // 2, HEIGHT - 40))
            screen.blit(salir_text, (3 * WIDTH // 4 - salir_text.get_width() // 2, HEIGHT - 40))

            pygame.display.flip()

    for nivel in niveles_en_carrera:
        resultado = jugar_nivel(nivel, personaje_idx)
        if resultado == "menu":
            main()
            return

    reproducir_musica(os.path.join(ruta_audio, "komiku_win.mp3"), loop=False)
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("¡Felicidades!", "Has completado todos los niveles.")
    main()

if __name__ == '__main__':
    main()
