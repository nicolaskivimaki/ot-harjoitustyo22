import os
import random
import pygame
dirname = os.path.dirname(__file__)

class Block(pygame.sprite.Sprite):

    def __init__(self, x, y, boost=False):
        super().__init__()
        if self.random_direction() == 1:
            self.move_right = True
        else:
            self.move_right = False
        if boost:
            self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "boost_block.png"))
        else:
            self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "block.png"))
        self.block = pygame.transform.smoothscale(self.image, (60, 10))
        self.rect = self.block.get_rect()
        self.rect.x = x
        self.rect.x = random.randint(0, 440)
        self.rect.y = y

    def random_direction(self):

        return random.randint(0,1)
    
    def get_block_y(self):

        return self.rect.y

    def move_block(self):

        speed = 1
        if self.rect.x < 1:
            self.move_right = True
        if self.rect.x > 440:
            self.move_right = False
        if self.move_right is True:
            self.rect.x += speed
        else:
            self.rect.x -= speed

    def camera_adjust_block(self, direction):

        self.rect.y += direction

    def draw_block(self, surface):
        pygame.draw.rect(surface, (211, 211, 211), self.rect)
