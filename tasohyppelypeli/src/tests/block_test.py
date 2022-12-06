import unittest
import pygame
from sprites.block import Block

class TestBlocks(unittest.TestCase):
    def setUp(self):
        self.block = Block(250, 250)

    def test_block_is_moving(self):
        self.block.move_block()
        self.assertNotEqual(str(self.block.rect.x), "250")
    
    def test_block_only_moves_sideways(self):
        self.block.move_block()
        self.assertEqual(str(self.block.rect.y), "250")
    
    def test_block_turns_on_right_side(self):
        did_not_turn = False
        for i in range(1000):
            self.block.move_block()
            if self.block.rect.x > 250 + 281:
                did_not_turn = True
            if self.block.rect.x < 250 - 281:
                did_not_turn = True

        self.assertEqual(str(did_not_turn), "False")
    
    def test_block_adjusts_for_camera_up(self):
        start_y = self.block.rect.y
        self.block.camera_adjust_block("u", 3)

        self.assertGreater(str(self.block.rect.y), f"{start_y}")

    def test_block_adjusts_for_camera_down(self):
        start_y = self.block.rect.y
        self.block.camera_adjust_block("d", 3)

        self.assertLess(str(self.block.rect.y), f"{start_y}")
    
    def test_block_draw(self):
        surface = pygame.display.set_mode((500, 600))
        surface.fill((255, 255, 255))

        self.block.draw_block(surface)

        assert surface.get_at((self.block.rect.x, self.block.rect.y)) == (211, 211, 211, 255)
        assert surface.get_at((self.block.rect.x + self.block.rect.width, self.block.rect.y + self.block.rect.height)) == (255, 255, 255, 255)