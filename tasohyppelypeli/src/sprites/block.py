import pygame
import random

class Block(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.counter = random.randint(80, 150)
        if self.random_direction() == 1:
            self.move_right = True
        else:
            self.move_right = False
        self.block = pygame.rect.Rect((x, y, 60, 10))
        self.block.x = x
        self.block.y = y
    
    def random_direction(self):
        return random.randint(0,1)
    
    def move_block(self):
        speed = 1
        if self.counter >= 220:
            self.move_right = False
        if self.counter <= 1:
            self.move_right = True
        if self.move_right == True:
            #self.block.move_ip(speed, 0)
            self.counter += 0.5
            self.block.x += speed
        else:
            #self.block.move_ip(-speed, 0)
            self.counter -= 0.5
            self.block.x -= speed
    
    def draw_block(self, surface):
        pygame.draw.rect(surface, (211, 211, 211), self.block)
