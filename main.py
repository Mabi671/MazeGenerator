import pygame # type: ignore
import time 
import sys
import random
import math

#pygame.init()

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


def generate_maze():
    max_i = screen_width // 50    
    max_j = screen_height // 50
    first_gate = random.randint(0, max_j - 1)
    second_gate = random.randint(0, max_j - 1)
    rott = 1
    for i in range(max_i - 1):
        for j in range(max_j):
            chance = random.randint(0, 6)
            if(chance == 2):
                rott = rott ^ 1
            if(i == 0 and first_gate == j or i == 0 and first_gate + 1 == j or i == max_i-2 and second_gate == j or i == max_i-2 and second_gate + 1 == j):
                rott = 1
                rect = Rect(25 - 20 * rott + i * 53, rott * 20  + j * 50,10, 70, rott, RED)
                rects.append(rect)
                continue
            rect = Rect(25 - 20 * rott + i * 50, rott * 20  + j * 50,10, 70, rott, BLUE)
            rects.append(rect)
            


class Rect:
    def __init__(self, x, y, width, height, rot, color):
        self.x = x
        self.y = y
        self.width = width - (width * rot) + (height * rot)
        self.height = height - (height * rot) + (width * rot)
        self.rect = pygame.Rect(x , y, width, height)
        self.color = color
        self.rot = rot
        self.rotate()
        self.rotated_surface = pygame.Surface((self.width, self.height))
    def rotate(self):
        rect_surface = pygame.Surface((self.width, self.height))  
        self.rotated_surface = pygame.transform.rotate(rect_surface, 90 * self.rot)
        self.rect = self.rotated_surface.get_rect(center=(self.x, self.y))
    def draw(self):
        self.rotated_surface.fill(self.color)
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