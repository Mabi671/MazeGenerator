import pygame # type: ignore
import time 
import pygame
import sys
import random
import math

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Window")
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (12, 12, 240)
rects = []
def draw():
    screen.fill(BLACK)
    for rect in rects:
        rect.draw()

def make_tunnel(n):
    for i in range(n):
        rect = Rect(250, 500 - (i * 55), 25, 50, False)
        rects.append(rect)
        rect = Rect(300, 500 - (i * 55), 25, 50, False)
        rects.append(rect)


class Rect:
    def __init__(self, x, y, width, height, ang):
        self.x = x
        self.y = y
        self.width = width - (width * ang) + (height * ang)
        self.height = height - (height * ang) + (width * ang)
        self.rect = pygame.Rect(x , y, width, height)
        self.color = BLUE
    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
    
    def upadateRect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

clock = pygame.time.Clock()
make_tunnel(5)
running = True
while running:
    clock.tick(2)
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            running = False
    draw()
    pygame.display.flip()


pygame.quit()
sys.exit()