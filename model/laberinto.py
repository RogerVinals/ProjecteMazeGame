import random

psiz = 50

paredes_lista_1 = [
    # Boundary walls (with opening at entrance (0,0))
    (0, 50, 20, 600),  # Left wall leaving gap from y=0 to 50 for entrance
    (70, 0, 880, 20),  # Top wall except entrance open at 0-20 x
    (0, 630, 900, 20),  # Bottom wall
    (880, 20, 20, 610),  # Right wall except bottom right exit open

    # Internal walls creating a more complex maze
    # Vertical walls
    (100, 20, 20, 400),
    (180, 230, 20, 400),
    (300, 0, 20, 350),
    (380, 170, 20, 400),
    (500, 20, 20, 330),
    (580, 310, 20, 320),
    (700, 0, 20, 600),
    # Horizontal walls
    (80, 500, 100, 20),
    (180, 230, 100, 20),
    (180, 350, 200, 20),
    (300, 490, 230, 20),
    (520, 100, 180, 20),
    (520, 430, 180, 20),
    (700, 580, 180, 20),
    # Additional small walls to make maze trickier
    (220, 120, 20, 130),
]
paredes_lista_2 = [
    (70,0,820,20),#Limite Superior
    (0,50,20,600),#Limite Izquierda
    (0,630,900,20),#Limite Abajo
    (880,0,20,650),#Limite Derecha
    #Creación del laberinto
    (psiz+20,20,20,590-psiz),
    (psiz+20,560,150,20),
    (220,230,20,350),
    (90,230,150,20),
    (90,210-psiz,200,20),
    (240+psiz,560,300,20),
    (240+psiz,210-psiz,20,400),

]
puerta1 = (100, 100, 200, 20)#Puerta Azul







