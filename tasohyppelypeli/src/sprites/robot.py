import os
import pygame
dirname = os.path.dirname(__file__)


class Robot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.rect.Rect((235, 570, 30, 30))
        self.image = pygame.image.load(os.path.join(dirname, "..", "assets", "robot.png"))
        self.block = pygame.transform.smoothscale(self.image, (10, 10))
        self.rect = self.block.get_rect()
        self.rect.x = 235
        self.rect.y = 570
        self.jumping = True
        self.jump_counter = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move_robot("l")
        if key[pygame.K_RIGHT]:
            self.move_robot("r")

    def move_robot(self, direction):
        distance = 2
        if direction == "l":
            self.rect.move_ip(-distance, 0)
        if direction == "r":
            self.rect.move_ip(distance, 0)

    def robot_jumping(self):

        speed = 3

        if self.jumping is True:
            self.rect.move_ip(0, -speed)
            self.jump_counter += 1
        else:
            self.jump_counter -= 1
            self.rect.move_ip(0, speed)

        if self.jump_counter > 60:
            self.jumping = False
        if self.jump_counter < 1:
            self.jumping = True

    def draw_robot(self, surface):
        pygame.draw.rect(surface, (0, 160, 0), self.rect)
