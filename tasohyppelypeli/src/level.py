import random
import pygame
from sprites.robot import Robot
from sprites.block import Block

class Level:

    """
    Level-luokka mahdollistaa ison osan pelin toiminnallisuudesta.
    Tämän luokan avulla voidaan hallita pelin alustoja sekä tutkia
    collisioneita.

    """

    def __init__(self):

        """
        Luodaan pelin robotti ja alustat ja säilötään näitä omissa
        sprite-ryhmissä.

        """
        self.robot = Robot()
        self.robot_group = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.boost_blocks = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.jumped_blocks = pygame.sprite.Group()
        self._initialize_sprites()

        self.score_counter = 0
        self.score_high = 0

    def _initialize_sprites(self):

        """
        Luo pelin ensimmäiset alustat.

        """

        block1 = Block(50, 440)
        block2 = Block(400, 300)
        block3 = Block(260, 210, boost=True)
        block4 = Block(100, 60)
        block5 = Block(0, 120)
        block6 = Block(0, 320)
        block7 = Block(0, -100, boost=True)
        block8 = Block(0, -260)
        block9 = Block(0, -400)

        all_blocks = [block1, block2, block3, block4, block5, block6, block7, block8, block9]

        for block in all_blocks:
            self.blocks.add(block)

        self.all_sprites.add(self.blocks, self.robot)
        self.robot_group.add(self.robot)
        self.boost_blocks.add(block3, block7)

    def create_blocks(self):

        """
        Luo loputonta virtaa hyppyalustoja. Jotkin alustat ovat
        korkeamman hypyn aiheuttavia boost-alustoja. Y-koordinaatti
        määrätään osittain satunnaisesti.

        """

        make_more_blocks = True
        for block in self.blocks:
            if block.rect.y < -200:
                make_more_blocks = False
        if make_more_blocks:

            block_y = random.randint(250, 350)
            if 293 < block_y < 308:
                new_block = Block(0, -block_y, boost=True)
                self.boost_blocks.add(new_block)
            else:
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

        if self.robot.get_robot_velocity() < 0:
            collision = pygame.sprite.spritecollide(self.robot, self.blocks, False)
            point_collision = pygame.sprite.spritecollide(self.robot, self.jumped_blocks, False)
            boost_collision = pygame.sprite.spritecollide(self.robot, self.boost_blocks, False)
            if boost_collision:
                self.robot.start_jump(boost=True)
            if collision and not boost_collision:
                self.robot.start_jump()
            if not point_collision:
                for block in collision:
                    self.jumped_blocks.add(block)

    def count_score(self):

        direction = self.robot.get_robot_velocity()

        if direction > 0:
            self.score_counter += 1
        if direction < 0:
            self.score_counter -= 1

        if self.score_counter // 5 > self.score_high:
            self.score_high = self.score_counter // 5

    def get_score(self):

        return self.score_high

    def adjust_camera(self):

        direction = self.robot.get_robot_last_move()

        if self.robot.rect.y < 336:

            for block in self.blocks:
                block.camera_adjust_block(direction)

            self.robot.robot_camera_adjust(direction)

        elif self.robot.rect.y > 336 and self.robot.velocity < 0 and len(self.jumped_blocks) > 1:

            for block in self.blocks:
                block.camera_adjust_block(direction)

            self.robot.robot_camera_adjust(direction)
