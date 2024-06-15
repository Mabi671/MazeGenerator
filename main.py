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

width, height = 10, 10
scale = 10.0
seed = 42

def generate_maze():    
    for i in range(screen_width // 50):
        for j in range(screen_height // 50):
            rott = random.randint(0, 1)
            rect = Rect(25 - 20 * rott + i * 50, rott * 20  + j * 50,10, 50, rott)
            rects.append(rect)


class Rect:
    def __init__(self, x, y, width, height, rot):
        self.x = x
        self.y = y
        self.width = width - (width * rot) + (height * rot)
        self.height = height - (height * rot) + (width * rot)
        self.rect = pygame.Rect(x , y, width, height)
        self.color = BLUE
        self.rot = rot
        self.rotate()
        self.rotated_surface = pygame.Surface((self.width, self.height))
    def rotate(self):
        rect_surface = pygame.Surface((self.width, self.height))  
        self.rotated_surface = pygame.transform.rotate(rect_surface, 90 * self.rot)
        self.rect = self.rotated_surface.get_rect(center=(self.x, self.y))
    def draw(self):
        self.rotated_surface.fill(BLUE)
        screen.blit(self.rotated_surface, self.rect.center)

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(3)
    for event in pygame.event.get():            
        if event.type == pygame.QUIT:
            running = False
    draw()
    rects = []
    generate_maze()
    
    pygame.display.flip()


pygame.quit()
sys.exit()