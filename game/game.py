import pygame
from config import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Event: QUIT")
                self.running = False
            elif event.type == pygame.KEYDOWN:
                print(f"Event: KEYDOWN - tlačítko: {pygame.key.name(event.key)}")
            elif event.type == pygame.KEYUP:
                print(f"Event: KEYUP - tlačítko: {pygame.key.name(event.key)}")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Event: MOUSEBUTTONDOWN - tlačítko: {event.button}, pozice: {event.pos}")
            elif event.type == pygame.MOUSEBUTTONUP:
                print(f"Event: MOUSEBUTTONUP - tlačítko: {event.button}, pozice: {event.pos}")
            elif event.type == pygame.MOUSEMOTION:
                print(f"Event: MOUSEMOTION - pozice: {event.pos}")
            elif event.type == pygame.MOUSEWHEEL:
                print(f"Event: MOUSEWHEEL - x: {event.x}, y: {event.y}")
            elif event.type == pygame.WINDOWFOCUSGAINED:
                print("Event: WINDOWFOCUSGAINED")
            elif event.type == pygame.WINDOWFOCUSLOST:
                print("Event: WINDOWFOCUSLOST")
            elif event.type == pygame.WINDOWEXPOSED:
                print("Event: WINDOWEXPOSED")
            elif event.type == pygame.WINDOWSHOWN:
                print("Event: WINDOWSHOWN")
            elif event.type == pygame.WINDOWMOVED:
                print(f"Event: WINDOWMOVED - pozice: ({event.x}, {event.y})")
            elif event.type == pygame.WINDOWRESIZED:
                print(f"Event: WINDOWRESIZED - velikost: ({event.x}, {event.y})")
            elif event.type == pygame.WINDOWENTER:
                print("Event: WINDOWENTER")
            elif event.type == pygame.WINDOWLEAVE:
                print("Event: WINDOWLEAVE")
            else:
                print(f"Event: {pygame.event.event_name(event.type)} (typ: {event.type})")
    
    def update(self):
        pass

    def draw(self):
        self.screen.fill(SKY_BLUE)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)