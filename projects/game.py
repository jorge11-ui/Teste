import pygame
from pygame.locals import *
from random import randint
import sys


# font = pygame.font.SysFont("jet brains mono", 70, bold=True)
# texto = font.render("PONG", True, color)
# centro = texto.get_rect(center=(400, 50))
class Window():
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.x = 800
        self.y = 800
        self.largura_bola = 20
        self.altura_bola = 20
        self.color = (255, 255, 255)
        
        self.screen = pygame.display.set_mode((self.x,self.y))
        
        self.start_pos = self.x // 2
        self.efeito_linha = 15
        self.largura_linha = 15
    def draw_line(self):
        for y in range(0, self.y, self.largura_linha + self.efeito_linha):
            pygame.draw.line(self.screen, self.color, (self.start_pos, y), (self.start_pos, y + 20), width=self.largura_linha)
        
            # screen.blit(texto, centro)

    def ball(self):
        if not hasattr(self.x, "speed_x"):
            self.speed_x *= 5
            self.speed_y = randint(-8, 8)

        self.bola = pygame.draw.circle(self.screen, self.color, (self.largura_bola, self.altura_bola), 15)
        self.direcao = 1
        self.speed_x = 5
        self.speed_y = 5

        self.largura_bola += self.speed_x
        self.altura_bola += self.speed_y

        if self.bola.left <= 0 or self.bola.right >= self.x:
            self.speed_x *= -1
            self.speed_y = randint(-8, 8) 
            while self.speed_y == 0:
                self.speed_y = randint(-8, 8)

            # if self.speed_x == 0: self.speed_y = 0
                # self.speed_x = randint(2, 8) * self.direcao
                # self.speed_y = randint(2, 8) * self.direcao

        if self.bola.top <= 0 or self.bola.bottom >= self.y:
            self.speed_y *= -1
            self.speed_x = randint(-8, 8) 
            while self.speed_x == 0:
                self.speed_x = randint(-8, 8)

        #colisao
        if self.bola.left <= 0 or self.bola.right >= self.x:
            self.speed_x *= -1
            self.speed_y = randint(-8, 8)
            while self.speed_y == 0:
                self.speed_y = randint(-8,8)

        if self.bola.top <= 0 or self.bola.bottom >= self.y:
            self.speed_y *= -1 
            
            self.speed_x = randint(-8, 8) 
            while self.speed_x == 0:
                self.speed_x = randint(-8, 8)



    def run(self):
        self.loop = True
        clock = pygame.time.Clock()
        while self.loop:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False
            self.screen.fill((0, 0, 0))
            self.draw_line()
            self.ball()
            pygame.display.flip()

        pygame.quit()
        quit()
    
if __name__ == "__main__":
    app = Window()
    app.run()
