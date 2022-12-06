import unittest
import pygame
from level import Level
from clock import Clock
from sprites.block import Block

class TestClock(unittest.TestCase):
    def setUp(self):
        self.clock = Clock()

    def test_clock_tick(self):
        self.clock.tick(60)
        assert self.clock.get_ticks() > 0
        assert isinstance(self.clock.get_ticks(), int)
        
class TestLevel(unittest.TestCase):
    def setUp(self):
        self.level = Level()

    def test_initializing_sprites_works(self):
        self.level._initialize_sprites()
        self.assertGreater(str(len(self.level.all_sprites)), "0")
        self.assertGreater(str(len(self.level.blocks)), "0")
        self.assertGreater(str(len(self.level.robot_group)), "0")