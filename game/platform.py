import pygame
from config import *

class Platform:
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)