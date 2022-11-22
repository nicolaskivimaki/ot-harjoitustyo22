import pygame

class Robot(object):
    def __init__(self):
        self.rect = pygame.rect.Rect((235, 570, 30, 30))
        self.jumping = True
        self.jump_counter = 0

    def handle_keys(self):
        key = pygame.key.get_pressed()
        distance = 2
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-distance, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(distance, 0)
    
    def robot_jumping(self):

        speed = 3
        
        if self.jumping == True:
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


import random

