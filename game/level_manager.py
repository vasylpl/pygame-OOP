"""
LevelManager - třída pro správu prvků na mapě
Odpovídá za:
- Vytváření platforem
- Vytváření coinů
- Vytváření nepřátel
"""

import pygame
from config import *
from game.platform import Platform
from game.coin import Coin
from game.enemy import Enemy
from game.smart_enemy import SmartEnemy

class LevelManager:
    def __init__(self, sprite_groups):
        """
        sprite_groups: dict s pygame.sprite.Group objekty
        Příklad: {'all': Group(), 'platforms': Group(), 'coins': Group(), 'enemies': Group()}
        """
        self.sprite_groups = sprite_groups
        self.platforms = []
        self.coins = []
        self.enemies = []
    
    def create_platforms(self):
        """Vytvoř všechny platformy na mapě"""
        # Podlaha
        ground = Platform(0, SCREEN_HEIGHT - 40, SCREEN_WIDTH, 40)
        self._add_platform(ground)
        
        # Další platformy
        platform1 = Platform(200, 600, 250, 20)
        self._add_platform(platform1)
        
        platform2 = Platform(600, 500, 250, 20)
        self._add_platform(platform2)
        
        platform3 = Platform(1000, 400, 200, 20)
        self._add_platform(platform3)
    
    def create_coins(self, total_coins=3):
        """Vytvoř všechny coiny na mapě"""
        for i in range(total_coins):
            coin = Coin(coin_id=i+1, total_coins=total_coins)
            self._add_coin(coin)
        return total_coins
    
    def create_enemies(self):
        """Vytvoř všechny nepřátele na mapě"""
        enemy = Enemy(400, 250)
        self._add_enemy(enemy)
        
        # Přidej Smart Enemy (Arauja)
        smart_enemy = SmartEnemy(800, 300)
        self._add_enemy(smart_enemy)
    
    def _add_platform(self, platform):
        """Přidej platformu do grupy a seznamu"""
        self.platforms.append(platform)
        self.sprite_groups['platforms'].add(platform)
        self.sprite_groups['all'].add(platform)
    
    def _add_coin(self, coin):
        """Přidej coin do grupy a seznamu"""
        self.coins.append(coin)
        self.sprite_groups['coins'].add(coin)
        self.sprite_groups['all'].add(coin)
    
    def _add_enemy(self, enemy):
        """Přidej nepřítele do grupy a seznamu"""
        self.enemies.append(enemy)
        self.sprite_groups['enemies'].add(enemy)
        self.sprite_groups['all'].add(enemy)
    
    def add_bonus_coin(self, x, y):
        """Přidej bonus coin na specifickou pozici"""
        bonus_coin = Coin(coin_id=len(self.coins)+1, total_coins=len(self.coins)+1)
        bonus_coin.rect.x = x
        bonus_coin.rect.y = y
        self._add_coin(bonus_coin)
    
    def remove_enemy(self, enemy):
        """Odstraň nepřítele ze hry"""
        self.enemies.remove(enemy)
        self.sprite_groups['enemies'].remove(enemy)
        self.sprite_groups['all'].remove(enemy)
