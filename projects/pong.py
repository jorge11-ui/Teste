import pygame
from pygame.locals import *
from random import randint
import sys

class Window:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.x = 800
        self.y = 800
        self.color = (255, 255, 255)
        
        self.screen = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("PONG")

        #texto
        self.font = pygame.font.SysFont("Fira code", 62, bold=True)
        self.texto = self.font.render("PONG",True, self.color)

        #linha do meio 
        self.start_pos = self.x // 2
        self.efeito_linha = 15
        self.largura_linha = 15
        
        self.raio_bola = 15
        self.bola_x = self.x // 2
        self.bola_y = self.y // 2
        self.speed_x = 5
        self.speed_y = 5

    def desenhar_linha(self):
        for y in range(0, self.y, self.largura_linha + self.efeito_linha):
            pygame.draw.line(self.screen, self.color, (self.start_pos, y), (self.start_pos, y + 20), width=self.largura_linha)

    def update_ball(self):
        # Atualiza a posição
        self.bola_x += self.speed_x
        self.bola_y += self.speed_y
    
        if self.bola_x - self.raio_bola <= 0 or self.bola_x + self.raio_bola >= self.x:
            self.speed_x *= -1
            
            self.speed_y += randint(-2, 2)
            
            self.speed_y = max(-10, min(10, self.speed_y))
            if self.speed_y == 0:
                self.speed_y = 1 
    
        if self.bola_y - self.raio_bola <= 0 or self.bola_y + self.raio_bola >= self.y:
            self.speed_y *= -1
            
            self.speed_x += randint(-2, 2)
            
            self.speed_x = max(-10, min(10, self.speed_x))
            if self.speed_x == 0:
                self.speed_x = 1
    def draw_ball(self):
       self.bola = pygame.draw.circle(
       self.screen,  
       self.color, 
       (int(self.bola_x), int(self.bola_y)), 
       self.raio_bola
        )

    def table(self):
        pass

    def run(self):
        self.loop = True
        clock = pygame.time.Clock()
        
        while self.loop:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.loop = False
                    
                #chamar as funcoes
            self.screen.fill((0, 0, 0))
            self.desenhar_linha()
            self.draw_ball()
            self.update_ball()
            pygame.display.flip()

        pygame.quit()
        sys.exit()
    
if __name__ == "__main__":
    app = Window()
    app.run()
