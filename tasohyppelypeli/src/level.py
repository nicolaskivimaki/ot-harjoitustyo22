import pygame
from sprites.robot import Robot
from sprites.block import Block

class Level:
    def __init__(self):
        self.robot = Robot()
        self.blocks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites()

    def _initialize_sprites(self):

        block1 = Block(50, 440)
        block2 = Block(400, 300)
        block3 = Block(260, 210)
        block4 = Block(100, 60)
        block5 = Block(0, 120)
        block6 = Block(-70, 320)

        all_blocks = [block1, block2, block3, block4, block5, block6]

        for block in all_blocks:
            self.blocks.add(block)

        self.all_sprites.add(self.blocks, self.robot)
