import pygame
import os
import math
from config import *
from game.base_enemy import BaseEnemy

class SmartEnemy(BaseEnemy):
    """
    Třída SmartEnemy - představuje inteligentního nepřítele (Arauja)
    
    - Běhá za hráčem
    - Umí skákat za hráčem
    - Když na něj skočíš → umře
    - Když tě chytne → umřeš
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        
        # Typ nepřítele
        self.enemy_type = "arauja"
        image_loaded = False
        try:
            image_path = os.path.join("assets", "Araujo.png")
            self.image = pygame.image.load(image_path).convert_alpha()
            self.image = pygame.transform.scale(self.image, (60, 60))
            print(f"Načten obrázek Smart Enemy: {image_path}")
            image_loaded = True
        except (pygame.error, FileNotFoundError):
            print(f"Obrázek Araujo.png nebyl nalezen")
        
        if not image_loaded:
            self.image = pygame.Surface((60, 60))
            self.image.fill((200, 0, 0))  # Červená barva
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        self.alive = True
        
        # Parametry AI
        self.speed = 2.5  # Rychlost běhání
        self.jump_cooldown = 0  # Cooldown mezi skoky
        self.jump_distance = 150  # Jak daleko skáče

    def update(self, player, platforms):
        """Aktualizuj pozici nepřítele - sleduj hráče"""
        
        # Snižuj cooldown
        if self.jump_cooldown > 0:
            self.jump_cooldown -= 1
        
        # Zjisti vzdálenost od hráče
        distance_x = player.rect.centerx - self.rect.centerx
        distance_y = player.rect.centery - self.rect.centery
        distance = math.sqrt(distance_x**2 + distance_y**2)
        
        # Běhej za hráčem
        if distance_x > 5:
            self.velocity_x = self.speed
        elif distance_x < -5:
            self.velocity_x = -self.speed
        else:
            self.velocity_x = 0
        
        # Skákej když je hráč blízko a výše
        if (abs(distance_x) < self.jump_distance and 
            player.rect.centery < self.rect.centery and 
            self.on_ground and 
            self.jump_cooldown == 0):
            self.velocity_y = -JUMP_POWER
            self.on_ground = False
            self.jump_cooldown = 30
        
        # Aplikuj gravitaci
        self.velocity_y += GRAVITY
        if self.velocity_y > 15:
            self.velocity_y = 15
        
        # Aplikuj pohyb
        self.rect.x += self.velocity_x
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
        
        # Zabránění vypadnutí ze mapy
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)
