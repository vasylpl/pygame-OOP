"""
GAME_STATE.PY - SPRÁVA STAVU HRY
=================================
Sleduje:
- Kolik coinů hráč sebrál
- Zda je hra vítězství nebo porážka
- Zprávy zobrazené hráči
- Zda hra běží nebo skončila
"""

class GameState:
    """Třída pro správu všech stavů a logiky hry"""
    
    def __init__(self, required_coins):
        """
        Inicializuj stav hry
        
        Args:
            required_coins: Kolik coinů je potřeba k vítězství
        """
        self.coins_collected = 0  # Počet sebráných coinů
        self.required_coins = required_coins  # Cíl: kolik coinů je potřeba
        self.game_won = False  # Zda vyhrál
        self.game_message = ""  # Zpráva na konci hry
        self.is_running = True  # Zda hra běží
    
    def add_coin(self):
        """Přidej jeden sebraný coin"""
        self.coins_collected += 1
    
    def add_coins(self, count):
        """Přidej více coinů najednou (např. při sběru více coinů)"""
        self.coins_collected += count
    
    def check_win_condition(self):
        """
        Zkontroluj jestli hráč vyhrál
        
        Returns:
            bool: True pokud sebrál všechny coiny, False jinak
        """
        return self.coins_collected >= self.required_coins
    
    def set_game_over(self, won=False, message=""):
        """
        Nastav konec hry s výsledkem
        
        Args:
            won: bool - True = vítězství, False = porážka
            message: string - zpráva kterou se hráči zobrazí
        """
        self.is_running = False
        self.game_won = won
        self.game_message = message
    
    def end_game_victory(self):
        """Konec hry - VÍTĚZSTVÍ!"""
        self.set_game_over(won=True, message="Sebral jsi všechny coiny!")
    
    def end_game_defeat(self, reason="Spadl jsi do propasti!"):
        """
        Konec hry - PORÁŽKA!
        
        Args:
            reason: Důvod porážky (text který se zobrazí)
        """
        self.set_game_over(won=False, message=reason)
    
    def reset(self, required_coins):
        """Resetuj stav pro novou hru - vyresetuj všechny proměnné"""
        self.__init__(required_coins)
