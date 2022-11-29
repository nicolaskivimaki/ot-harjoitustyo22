import unittest
from sprites.robot import Robot

class TestBlocks(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()

    def test_robot_is_jumping(self):
        self.robot.robot_jumping()
        self.assertLess(str(self.robot.rect.y), "570")
    
    def test_robot_comes_down_after_jump(self):
        over = False
        for i in range(1000):
            self.robot.robot_jumping()
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