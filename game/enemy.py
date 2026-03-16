import pygame
import os
import random
from config import *
from game.base_enemy import BaseEnemy

class Enemy(BaseEnemy):
    """
    Třída Enemy - představuje nepřítele (Koundého)
    
    - Pohybuje se zleva doprava
    - Když na něj skočíš → umře
    - Když tě chytne → umřeš
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        
        # Typ nepřítele
        self.enemy_type = "kounde"
        image_loaded = False
        try:
            image_path = os.path.join("assets", "Kounde.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (60, 60))
            print(f"Načten obrázek nepřítele: {image_path}")
            image_loaded = True
        except (pygame.error, FileNotFoundError):
            print(f"Obrázek Kounde.png nebyl nalezen")
        
        if not image_loaded:
            self.image = pygame.Surface((60, 60))
            self.image.fill((100, 0, 0))  # Tmavě červená barva
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.velocity_x = 3  # Pohyb zleva doprava
        self.velocity_y = 0
        self.on_ground = False
        self.alive = True
        
        # Náhodný pohyb
        self.direction_change_timer = 0
        self.change_direction_interval = random.randint(30, 90)  # Změní směr každých 30-90 frames

    def update(self, platforms):
        """Aktualizuj pozici nepřítele"""
        
        # Náhodná logika pohybu
        self.direction_change_timer += 1
        if self.direction_change_timer >= self.change_direction_interval:
            # Vyber náhodný směr nebo stoj na místě
            random_choice = random.randint(0, 2)
            if random_choice == 0:
                self.velocity_x = 3  # Jdi doprava
            elif random_choice == 1:
                self.velocity_x = -3  # Jdi doleva
            else:
                self.velocity_x = 0  # Stoj na místě
            
            # Reset timer a vyber nový interval
            self.direction_change_timer = 0
            self.change_direction_interval = random.randint(30, 90)
        
        self.rect.x += self.velocity_x
        
        # Odraz od okrajů
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.velocity_x *= -1
        
        # Gravitace
        self.velocity_y += GRAVITY
        if self.velocity_y > 15:
            self.velocity_y = 15
        
        self.rect.y += self.velocity_y
        self.on_ground = False
        
        # Kolize s platformami
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                elif self.velocity_y < 0:
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
