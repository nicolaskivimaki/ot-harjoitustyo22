import unittest
from sprites.block import Block

class TestBlocks(unittest.TestCase):
    def setUp(self):
        self.block = Block(250, 250)

    def test_block_is_moving(self):
        self.block.move_block()
        self.assertNotEqual(str(self.block.block.x), "250")
    
    def test_block_only_moves_sideways(self):
        self.block.move_block()
        self.assertEqual(str(self.block.block.y), "250")
    
    def test_block_turns(self):
        did_not_turn = False
        for i in range(1000):
            self.block.move_block()
            if self.block.block.x > 250 + 281:
                did_not_turn = True
            if self.block.block.x < 250 - 281:
                did_not_turn = True

        self.assertEqual(str(did_not_turn), "False")