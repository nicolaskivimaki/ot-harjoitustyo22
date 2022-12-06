import unittest
import pygame
import pygame.locals
from sprites.robot import Robot

class TestBlocks(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.robot = Robot()

    def test_robot_is_jumping_in_beginning(self):
        self.robot.robot_jumping(first_jumps=True)
        self.assertLess(str(self.robot.rect.y), "570")
    
    def test_robot_jumps_when_not_first_jumps(self):
        self.robot.robot_jumping(first_jumps=False)
        self.assertLess(str(self.robot.rect.y), "570")
    
    def test_robot_comes_down_after_jump(self):
        over = False
        for i in range(1000):
            self.robot.robot_jumping(first_jumps=True)
            if self.robot.rect.y > 570:
                over = True
            if self.robot.rect.y < 200:
                over = True

        self.assertEqual(str(over), "False")
    
    def test_robot_can_move_to_the_right(self):
        self.robot.move_robot("r")
        self.assertGreater(str(self.robot.rect.x), "235")
    
    def test_robot_can_move_to_the_left(self):
        self.robot.move_robot("l")
        self.assertLess(str(self.robot.rect.x), "235")

    def test_start_jump_works(self):
        self.robot.jumping == False
        self.robot.start_jump()
        self.assertEqual(str(self.robot.jumping), "True")

    def test_returns_last_move(self):
        self.assertEqual(str(self.robot.get_robot_last_move()), "u")
        
    def test_returns_speed(self):
        self.assertEqual(str(self.robot.get_robot_speed()), "3")
    
    def test_returns_robot_y(self):
        self.assertEqual(str(self.robot.get_robot_y()), "570")

    def test_robot_adjusts_for_camera_down(self):
        start_y = self.robot.rect.y
        self.robot.robot_camera_adjust("d")

        self.assertLess(str(self.robot.rect.y), f"{start_y}")

    def test_robot_adjusts_for_camera_up(self):
        start_y = self.robot.rect.y
        self.robot.robot_camera_adjust("u")

        self.assertGreater(str(self.robot.rect.y), f"{start_y}")
    
    def test_robot_draw(self):
        surface = pygame.display.set_mode((500, 600))
        surface.fill((255, 255, 255))

        self.robot.draw_robot(surface)

        assert surface.get_at((self.robot.rect.x, self.robot.rect.y)) == (0, 160, 0, 255)
        assert surface.get_at((self.robot.rect.x + self.robot.rect.width, self.robot.rect.y + self.robot.rect.height)) == (255, 255, 255, 255)
        