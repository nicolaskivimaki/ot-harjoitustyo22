import pygame
from sprites.robot import Robot
from sprites.block import Block
import random

class Level:

    def __init__(self):
        self.robot = Robot()
        self.robot_group = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.jumped_blocks = pygame.sprite.Group()
        self._initialize_sprites()

        self.score_counter = 0
        self.score_high = 0

    def _initialize_sprites(self):

        block1 = Block(50, 440)
        block2 = Block(400, 300)
        block3 = Block(260, 210)
        block4 = Block(100, 60)
        block5 = Block(0, 120)
        block6 = Block(0, 320)
        block7 = Block(0, -100)
        block8 = Block(0, -260)
        block9 = Block(0, -400)

        all_blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9]

        for block in all_blocks:
            self.blocks.add(block)

        self.all_sprites.add(self.blocks, self.robot)
        self.robot_group.add(self.robot)
    
    def create_blocks(self):
        make_more_blocks = True
        for block in self.blocks:
            if block.rect.y < -200:
                make_more_blocks = False
        if make_more_blocks:
            block_y = random.randint(250, 350)
            new_block = Block(0, -block_y)
            self.blocks.add(new_block)
            self.all_sprites.add(new_block)
    
    def delete_old_blocks(self):
        for block in self.blocks:
            if block.rect.y > 800:
                self.blocks.remove(block)
                self.all_sprites.remove(block)
                

    def move_sprites(self):

        for block in self.blocks:
                block.move_block()
        self.check_collisions()
        self.robot.handle_keys()
        if len(self.jumped_blocks) == 0:
            self.robot.robot_jumping(first_jumps=True)
        else:
            self.robot.robot_jumping(first_jumps=False)

    def check_collisions(self):

        if self.robot.jumping == False:
            collision = pygame.sprite.spritecollide(self.robot, self.blocks, False)
            point_collision = pygame.sprite.spritecollide(self.robot, self.jumped_blocks, False)
            if collision:
                self.robot.start_jump()
            if not point_collision:
                for block in collision:
                    self.jumped_blocks.add(block)
    
    def count_score(self):

        direction = self.robot.get_robot_last_move()

        if direction == "u":
            self.score_counter += 1
        if direction == "d":
            self.score_counter -= 1
        
        if self.score_counter // 10 > self.score_high:
            self.score_high = self.score_counter // 10
        
    def get_score(self):

        return self.score_high
    
    def adjust_camera(self):
        direction = self.robot.get_robot_last_move()
        speed = self.robot.get_robot_speed()

        if (self.robot.rect.y >= 335 and direction == "u") or len(self.jumped_blocks) < 1:
            return
        
        else:
            for block in self.blocks:
                block.camera_adjust_block(direction, speed)
            
            self.robot.robot_camera_adjust(direction)

                
