import pygame
import os
from config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        image_loaded = False

        for name in ["brochacho", "player"]:
            for ext in ["png", "jpg", "jpeg", "webp"]:
                try:
                    image_path = os.path.join("img", f"{name}.{ext}")
                    self.image = pygame.image.load(image_path).convert_alpha
                    self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
                    print(f"Načten obrázek hráče: {image_path}")
                    image_loaded = True

                    break

                except(pygame.error, FileNotFoundError):
                    continue
            
        if not image_loaded:
            self.image = pygame([PLAYER_WIDTH, PLAYER_HEIGHT])
            self.image = self.image.fill(PLAYER_COLOR)

            self.image = self.image.get.rect()
            self.rect.x = x
            self.rect.y = y

            self.velocity.x = 0
            self.velocity.y = 0

            self.on_ground = False

        def update(self, platforms):
            key = pygame.key.get.press()
            self.velocity_x = 0

            if key[pygame.K_right]:
                self.velocity_x = PLAYER_SPEED
            
            if key[pygame.K_space] and self.on_ground:
                self.velocity_y = -JUMP_POWER
                self.on_ground = False