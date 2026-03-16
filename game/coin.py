import pygame
import random
from config import *

class Coin(pygame.sprite.Sprite):
    """
    Třída Coin - představuje jednu minci kterou hráč sbírá
    
    Vlastnosti:
    - Malý žlutý kruh (sprite)
    - Náhodná pozice v každé hře
    - Když hráč sebere všechny, hra se uspěšně skončí
    """

    def __init__(self, coin_id=1, total_coins=3):
        """
        Inicializuj coin
        
        Args:
            coin_id: ID coinu (1, 2, 3...)
            total_coins: Celkový počet coinů na mapě
        """
        super().__init__()  # Zavolej rodičovský konstruktor (pygame.sprite.Sprite)
        
        # Vytvoř grafiku - žlutý kruh
        # pygame.SRCALPHA = průhledné pozadí (alfa kanál)
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        
        # Nakresli zlatý kruh do obrázku
        # pygame.draw.circle(surface, barva, střed, radius)
        pygame.draw.circle(self.image, (255, 215, 0), (10, 10), 10)  # Zlatý kruh
        
        # Vytvořit rectangle pro fyziku (kolize, pozice)
        self.rect = self.image.get_rect()
        
        # Informace o coinu
        self.coin_id = coin_id
        self.total_coins = total_coins
        
        # Náhodná pozice - vyhni se hornímu a dolnímu okraji
        # random.randint(min, max) = náhodné číslo včetně obou mezí
        self.rect.x = random.randint(20, SCREEN_WIDTH - 40)
        self.rect.y = random.randint(200, SCREEN_HEIGHT - 150)

    def draw(self, screen):
        """
        Vykresli coin na obrazovku
        
        Args:
            screen: pygame Surface (herní okno)
        """
        # screen.blit() = "namaluj obrázek na obrazovku"
        screen.blit(self.image, self.rect)
