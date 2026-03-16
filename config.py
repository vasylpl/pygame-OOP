# ===== HERNÍ NASTAVENÍ =====
# Všechny konstanty a konfigurace hry na jednom místě

# Rozměry okna (pixely)
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1200

# Barvy (RGB formát: Red, Green, Blue - hodnoty 0-255)
SKY_BLUE = (100, 150, 255)  # Modrý nebes
FPS = 60  # Frames per second - plynulost hry

# Barva platforem
PLATFORM_COLOR = (50, 200, 50)  # Zelená

# Parametry hráče (ViniJR)
PLAYER_WIDTH = 80  # Šířka hráče v pixelech
PLAYER_HEIGHT = 80  # Výška hráče v pixelech
PLAYER_COLOUR = (255, 50, 50)  # Červená (fallback když se obrázek nenačte)
PLAYER_SPEED = 5  # Rychlost pohybu doleva/doprava
JUMP_POWER = 15  # Síla skoku

# Fyzika
GRAVITY = 0.8  # Gravitační zrychlení - jak moc padá