import pygame

pygame.init()
#variaveis
tamanho = 800, 800
altura, largura = tamanho
#code-here
color = (200, 140, 10)
screen = pygame.display.set_mode(tamanho)
clock = pygame.time.Clock()

pygame.display.update()
loop = True
while loop :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        screen.fill((0, 0, 255))
        pygame.draw.circle(screen, (255, 0, 0), (400, 200), 100)

pygame.quit()
