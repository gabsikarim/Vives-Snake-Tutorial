import random
import sys
from typing import List

import pygame
from pygame.locals import *

class Game:
    def __init__(self, name: str, width: int =500, height: int =500):
        pygame.init()
        self.primary_font = pygame.font.SysFont("Calibri", 20)
        pygame.display.set_caption(name)
        self.display = pygame.display.set_mode((width, height), RESIZABLE)

    def message(self, msg):
        self.display.fill((0, 0, 0)) # Scherm volledig zwart maken.

        mesg = pygame.font.Font.render(self.primary_font, msg, True, (255, 255, 255))
        mesg_rect = mesg.get_rect(center=pygame.display.get_surface().get_rect().center)
        self.display.blit(mesg, mesg_rect)

    def run(self):
        self.message("Press SPACE")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        words: List[str] = ["Welkom op de management days!",
                                            "Ready to build a snake game?",
                                            "Why does a python live on land...? Because it is above C level!"]
                        self.message(msg=random.choice(words))
            pygame.display.update()

if __name__ == '__main__':
    # Extra info over pygame: https://www.pygame.org/docs/
    try:
        myGame = Game(name="My First Game!")
        myGame.run()
    except Exception as ex:
        print(ex)
    finally:
        print("closing up...")
        pygame.quit()
        sys.exit()
