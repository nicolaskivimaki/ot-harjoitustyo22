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
        self.speed = 3
        self.jumping = True
        self.can_fall = False
        self.jump_counter = 0
        self.last_move = "u"

    def handle_keys(self):

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.move_robot("l")
        if key[pygame.K_RIGHT]:
            self.move_robot("r")

    def move_robot(self, direction):

        if direction == "l":
            self.rect.move_ip(-self.speed, 0)
        if direction == "r":
            self.rect.move_ip(self.speed, 0)

    def robot_jumping(self, first_jumps):

        speed = 3

        if self.jumping is True:
            self.rect.move_ip(0, -speed)
            self.last_move = "u"
            self.jump_counter += 1
        else:
            self.jump_counter -= 1
            self.rect.move_ip(0, speed)
            self.last_move = "d"

        if self.jump_counter > 60:
            self.jumping = False
        if first_jumps:
            if self.jump_counter < 1:
                self.jumping = True
    
    def start_jump(self):

        self.jump_counter = 0
        self.jumping = True
    
    def get_robot_last_move(self):

        return self.last_move
    
    def get_robot_speed(self):

        return self.speed
    
    def get_robot_y(self):

        return self.rect.y
    
    def robot_camera_adjust(self, direction):
        if direction == "u":
            self.rect.move_ip(0, self.speed)
        if direction == "d":
            self.rect.move_ip(0, -self.speed)

    def draw_robot(self, surface):

        pygame.draw.rect(surface, (0, 160, 0), self.rect)
