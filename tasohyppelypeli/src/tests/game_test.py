import unittest
import pygame
import sys
from ui.level import Level
from game_loop import GameLoop
from features.event_que import EventQueue
from features.renderer import Renderer
from features.button import Button
from features.clock import Clock
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

    def test_point_calculator_works(self):
        self.level._initialize_sprites()
        for i in range(100):
            self.level.move_sprites()
            self.level.count_score()
        self.assertGreater(str(self.level.score_high), "0") 

class TestButton(unittest.TestCase):
    def test_init(self):
        button = Button(100, 200, 300, 400, text="Click me", font_size=24, border_width=4)
        assert button.x == 100
        assert button.y == 200
        assert button.width == 300
        assert button.height == 400
        assert button.text == "Click me"
        assert button.font_size == 24
        assert button.border_width == 4