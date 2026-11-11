import pygame as pg
import random
import sys

pg.init()
Altura, Largura = 800, 600

#::::CORES
verde = (0, 255, 0)
amarelo = (255, 255, 0)
azul = (173, 216, 230)
screen = pg.display.set_mode((Altura, Largura))

lista_estrelas = []
for i in range(100):
    x_aleatorio = random.randint(0, 800)
    y_aleatorio = random.randint(0, 480)
    lista_estrelas.append((x_aleatorio, y_aleatorio))
sol_x = 750
vel_sol = 3
cor_ceu = azul
clock = pg.time.Clock()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    sol_x -= vel_sol
    if sol_x <= 0:
        cor_ceu = (0, 0, 0)
    screen.fill((cor_ceu))

    if sol_x <= 0:
        for estrelas in lista_estrelas:
            pg.draw.circle(screen, (255, 255, 255), estrelas, 3)


    pg.draw.circle(screen, amarelo, ( sol_x, 50,), 80)
    pg.draw.rect(screen, verde, (0, 500, 800, 500))
    pg.draw.rect(screen, verde, (200, 300, 15, 250))
    pg.draw.circle(screen, verde, (200, 250,),50 )
    pg.draw.circle(screen, verde, (240, 280,),50 )
    pg.draw.circle(screen, verde, (160, 310,),50 )

    pg.display.flip()
    clock.tick(60)
pg.quit()
sys.exit()
