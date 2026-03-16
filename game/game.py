from os import name
import pygame
from config import *
from game.player import Player
from game.platform import Platform
from game.coin import Coin
from game.enemy import Enemy
from game.game_state import GameState
from game.level_manager import LevelManager

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        # Sprite grupy
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        sprite_groups = {
            'all': self.all_sprites,
            'platforms': self.platforms,
            'coins': self.coins,
            'enemies': self.enemies
        }
        
        # Inicializuj level manager
        self.level_manager = LevelManager(sprite_groups)
        
        # Inicializuj hráče
        self.player = Player(100, 100)
        self.all_sprites.add(self.player)
        
        # Vytvoř platformy
        self.level_manager.create_platforms()
        
        # Vytvoř coiny a nepřátele
        total_coins = self.level_manager.create_coins(total_coins=3)
        self.level_manager.create_enemies()
        total_enemies = len(self.level_manager.enemies)  # 2 nepřátelé
        
        # Inicializuj game state
        # Musíš porazit všechny nepřátele (2) a sebrat všechny coiny (3 + 2 bonus = 5)
        self.game_state = GameState(required_coins=total_coins + total_enemies)
        
        # Pause menu
        self.is_paused = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.is_running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # ESC pro pause menu
                    self.is_paused = not self.is_paused
    
    def update(self):
        # Aktualizuj hráče
        player_fell = self.player.update(self.platforms)
        if player_fell:
            self.game_state.end_game_defeat("Spadl jsi do propasti!")
            return

        # Aktualizuj nepřítele
        for enemy in self.level_manager.enemies:
            # SmartEnemy (arauja) dostane i informaci o hráči
            if enemy.get_type() == "arauja":
                enemy.update(self.player, self.platforms)
            else:
                enemy.update(self.platforms)

        # Kontrola kolize s nepřítelem
        for enemy in self.level_manager.enemies[:]:  # Použij copy seznamu aby se dalo modifikovat
            if self.player.rect.colliderect(enemy.rect):
                # Pokud skočíš nepříteli na hlavu (hráč padá dolů)
                if self.player.velocity_y > 0 and self.player.rect.bottom <= enemy.rect.centery:
                    enemy_name = enemy.get_type().capitalize()
                    self.level_manager.remove_enemy(enemy)
                    self.player.velocity_y = -JUMP_POWER  # Skok po zabití
                    
                    # Vytvoř bonus coin na místě kde byl nepřítel
                    self.level_manager.add_bonus_coin(enemy.rect.centerx - 10, enemy.rect.centery - 10)
                else:
                    # Nepřítel tě chytil - GAME OVER
                    enemy_name = enemy.get_type().capitalize()
                    message = f"{enemy_name} ti strčil tě do kapsy!"
                    self.game_state.end_game_defeat(message)
                    return

        # Kontrola sběru coinů
        coins_hit = pygame.sprite.spritecollide(self.player, self.coins, True)
        self.game_state.add_coins(len(coins_hit))

        # Pokud sebral všechny coiny, hra skončila úspěšně
        if self.game_state.check_win_condition():
            self.game_state.end_game_victory()

    def draw(self):
        self.screen.fill(SKY_BLUE)
        for sprite in self.all_sprites:
            sprite.draw(self.screen)
        pygame.display.flip()

    def show_pause_menu(self):
        """Zobraz pause menu"""
        font_large = pygame.font.Font(None, 60)
        font_small = pygame.font.Font(None, 30)
        
        waiting = True
        while waiting and self.is_paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_state.is_running = False
                    return False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # ESC pro zpět do hry
                        self.is_paused = False
                        waiting = False
                    elif event.key == pygame.K_r:  # R pro restart
                        return True
                    elif event.key == pygame.K_q:  # Q pro quit
                        self.game_state.is_running = False
                        return False
            
            # Vykreslení pause screenu
            self.screen.fill(SKY_BLUE)
            
            pause_text = font_large.render("⏸ PAUZA ⏸", True, (255, 255, 0))
            resume_text = font_small.render("Stiskni [ESC] - POKRAČOVAT", True, (255, 255, 255))
            restart_text = font_small.render("Stiskni [R] - RESTARTOVAT", True, (255, 255, 255))
            quit_text = font_small.render("Stiskni [Q] - UKONČIT", True, (255, 255, 255))
            
            pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, 200))
            resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 420))
            quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, 490))
            
            self.screen.blit(pause_text, pause_rect)
            self.screen.blit(resume_text, resume_rect)
            self.screen.blit(restart_text, restart_rect)
            self.screen.blit(quit_text, quit_rect)
            
            pygame.display.flip()
            self.clock.tick(30)
        
        return None

    def show_end_screen(self):
        """Zobraz end screen s možností hrát znovu nebo ukončit"""
        font_large = pygame.font.Font(None, 60)
        font_medium = pygame.font.Font(None, 40)
        font_small = pygame.font.Font(None, 30)
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # R pro restart
                        return True
                    elif event.key == pygame.K_q:  # Q pro quit
                        return False
            
            # Vykreslení end screenu
            self.screen.fill(SKY_BLUE)
            
            if self.game_state.game_won:
                # VÍTĚZSTVÍ
                title = font_large.render("🎉 VÍTĚZSTVÍ! 🎉", True, (255, 215, 0))
                message = font_medium.render("Sebral jsi všechny coiny!", True, (0, 255, 0))
            else:
                # GAME OVER
                title = font_large.render("💀 GAME OVER! 💀", True, (255, 0, 0))
                if self.game_state.game_message:
                    message = font_medium.render(self.game_state.game_message, True, (255, 100, 100))
                else:
                    message = font_medium.render("Spadl jsi do propasti!", True, (255, 100, 100))
            
            # Tlačítka
            restart_text = font_small.render("Stiskni [R] - HRÁT ZNOVU", True, (255, 255, 255))
            quit_text = font_small.render("Stiskni [Q] - UKONČIT HRU", True, (255, 255, 255))
            
            # Vycentrování textu
            title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 100))
            message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, 200))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, 350))
            quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, 420))
            
            self.screen.blit(title, title_rect)
            self.screen.blit(message, message_rect)
            self.screen.blit(restart_text, restart_rect)
            self.screen.blit(quit_text, quit_rect)
            
            pygame.display.flip()
            self.clock.tick(30)

    def run(self):
        while self.game_state.is_running:
            self.handle_events()
            
            # Pokud je hra pozastavená, zobraz pause menu
            if self.is_paused:
                pause_result = self.show_pause_menu()
                if pause_result is True:  # Restart
                    return True
                elif pause_result is False:  # Quit
                    return False
                continue  # Jdi zpět na začátek loopu
            
            self.update()
            self.draw()
            self.clock.tick(FPS)

        # Zobraz end screen
        return self.show_end_screen()