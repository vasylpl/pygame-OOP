"""
MAIN.PY - VSTUPNÍ BOD APLIKACE
============================
Spouští hru a zajišťuje možnost hraní více her za sebou bez restartování
"""

import pygame
from config import *  # Import všech konstant
from game.game import Game

def main():
    """Hlavní funkce programu"""
    
    # Inicializuj Pygame knihovnu
    pygame.init()
    
    # Vytvoř herní okno
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("ViniJR - Platformer Game")  # Název okna

    # Smyčka která umožňuje hrát znovu bez restartování programu
    play_again = True
    while play_again:
        # Vytvoř novou hru
        game = Game(screen)
        
        # Spusť hru a čekej na výsledek
        # game.run() vrátí True (chceš hrát znovu) nebo False (chceš ukončit)
        game.run()
        
        # show_end_screen() vrátí True (restart) nebo False (quit)
        play_again = game.show_end_screen()

    # Ukonči Pygame (čištění paměti)
    pygame.quit()

# Standardní Python spouštěcí bod
if __name__ == "__main__":
    main()