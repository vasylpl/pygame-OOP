"""
BaseEnemy - abstraktní třída pro všechny nepřítele
Zajistí konzistentní interface pro všechny typy nepřátel
"""

import pygame
from config import *

class BaseEnemy(pygame.sprite.Sprite):
    """Abstraktní třída pro nepřítele"""
    
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 60, 60)
        self.alive = True
        self.enemy_type = "base"  # Override v podtřídách
    
    def update(self, *args, **kwargs):
        """Musí být implementováno v podtřídách"""
        raise NotImplementedError("update() musí být implementováno")
    
    def draw(self, screen):
        """Musí být implementováno v podtřídách"""
        raise NotImplementedError("draw() musí být implementováno")
    
    def get_type(self):
        """Vrátí typ nepřítele"""
        return self.enemy_type
