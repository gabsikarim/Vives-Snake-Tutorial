import enum
import random
import sys

import pygame
from pygame.locals import *

class Movement(enum.Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

class Snake:
    def __init__(self, blocksize=50):
        self.head = pygame.Rect((0, 0), (blocksize, blocksize))
        self.tail = []
        self.length = 0
        self.blocksize = blocksize
        self.last_move = Movement.UP

    @property
    def movement(self):
        return self.last_move

    @movement.setter
    def movement(self, next_move):
        valid_move = True
        if next_move == Movement.LEFT and self.last_move != Movement.RIGHT:
            self.head.left -= self.blocksize
        elif next_move == Movement.RIGHT and self.last_move != Movement.LEFT:
            self.head.left += self.blocksize
        elif next_move == Movement.UP and self.last_move != Movement.DOWN:
            self.head.top -= self.blocksize
        elif next_move == Movement.DOWN and self.last_move != Movement.UP:
            self.head.top += self.blocksize
        else:
            valid_move = False
            #self.movement = self.last_move

        if valid_move:
            self.last_move = next_move

    def set_position(self, x, y):
        self.head.left = x
        self.head.top = y

    def get_position(self):
        return self.head.left, self.head.top

    def __eq__(self, other):
        return self.get_position() == other.get_position()

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

    def game_init(self):
        self.snake = Snake()
        self.snake.set_position(self.display.get_width() / 2, self.display.get_height() / 2)
        self.running = True

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

    def draw_snake(self):
        pygame.draw.rect(self.display, (255, 255, 255), self.snake.head)

    def draw_objects(self):
        self.display.fill((0, 0, 0))
        #self.draw_food()
        self.draw_snake()

    def start(self):
        self.game_init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_KP_4:
                        self.snake.movement = Movement.LEFT
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP_6:
                        self.snake.movement = Movement.RIGHT
                    elif event.key == pygame.K_UP or event.key == pygame.K_KP_8:
                        self.snake.movement = Movement.UP
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_KP_2:
                        self.snake.movement = Movement.DOWN

            self.draw_objects()
            pygame.display.update()




if __name__ == '__main__':
    try:
        sg = SnakeGame("Example 2 - Snake object")
        sg.start()
    except Exception as ex:
        print(ex)
    finally:
        print("closing up...")
        pygame.quit()
        sys.exit()
