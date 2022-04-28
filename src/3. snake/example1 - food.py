import random
import sys

import pygame
from pygame.locals import *

class Food:
    def __init__(self, blocksize=50, img_src="img/vives_logo.bmp"):
        self.blocksize = 50
        self.image = pygame.transform.scale(pygame.image.load(img_src), (blocksize, blocksize))
        self.rect = self.image.get_rect()

    def set_position(self, x, y):
        self.rect.left = x
        self.rect.top = y

    def get_position(self):
        return self.rect.left, self.rect.top

class SnakeGame:
    def __init__(self, name: str, width: int =500, height: int =500):
        pygame.init()
        self.primary_font = pygame.font.SysFont("Calibri", 20)
        pygame.display.set_caption(name)
        self.display = pygame.display.set_mode((width, height), RESIZABLE)
        self.food = self.spawn_food()

    def message(self, msg):
        mesg = pygame.font.Font.render(self.primary_font, msg, True, (255, 255, 255))
        mesg_rect = mesg.get_rect(center=pygame.display.get_surface().get_rect().center)
        self.display.blit(mesg, mesg_rect)

    def spawn_food(self):
        f = Food()
        fx = round(random.randrange(0, self.display.get_width() - f.blocksize) / f.blocksize) * f.blocksize
        fy = round(random.randrange(0, self.display.get_height() - f.blocksize) / f.blocksize) * f.blocksize
        f.set_position(x=fx, y=fy)
        return f

    def draw_food(self):
        self.display.blit(self.food.image, (self.food.rect.left, self.food.rect.top))

    def draw_objects(self):
        self.display.fill((0, 0, 0))
        self.draw_food()

    def start(self):
        self.message("Press SPACE")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.food = self.spawn_food()
            self.draw_objects()
            pygame.display.update()


if __name__ == '__main__':
    try:
        sg = SnakeGame("Example 1 - Food")
        sg.start()
    except Exception as ex:
        print(ex)
    finally:
        print("closing up...")
        pygame.quit()
        sys.exit()
