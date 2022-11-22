import pygame
from sprites.robot import Robot
from sprites.block import Block

pygame.init()
screen = pygame.display.set_mode((500, 600))
screen.fill((255, 255, 255))
pygame.display.set_caption("Tasohyppelypeli")
robot = Robot()
block1 = Block(50, 440)
block2 = Block(400, 300)
block3 = Block(260, 210)
block4 = Block(100, 60)
block5 = Block(0, 120)
block6 = Block(-70, 320)
all_blocks = [block1, block2, block3, block4, block5, block6]
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    robot.draw_robot(screen)
    for block in all_blocks:
        block.move_block()
        block.draw_block(screen)
    robot.handle_keys()
    robot.robot_jumping()
    pygame.display.update()
    clock.tick(90)

pygame.quit()