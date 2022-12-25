import sys
import pygame
from pygame.locals import *
from start_screen import StartScreen
from end_screen import EndScreen
from leaderboard import LeaderBoard

class GameLoop:

    def __init__(self, level, renderer, event_queue, clock):
        self._level = level
        self._beginning_screen = StartScreen()
        self._end_screen = EndScreen()
        self._leaderboard = LeaderBoard()
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock
        self.game_state = "START"

    def start(self):

        while True:

            mouse_pos = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

            if self.game_state == "START":
                self.start_screen(mouse_pos)

            if self.game_state == "PLAYING":
                self.game_loop()

            if self.game_state == "GAME OVER":
                self.game_over()

            self._clock.tick(60)
    
    def start_screen(self, mouse_pos=None):
        button = self._beginning_screen._button
        if mouse_pos:
            if button.x <= mouse_pos[0] <= button.x + button.width and button.y <= mouse_pos[1] <= button.y + button.height:
                self.game_state = "PLAYING"
        heading = self._beginning_screen.heading_text()
        heading_pos = self._beginning_screen._heading_pos
        self._renderer.render_blank_screen()
        self._renderer.render_text(heading, heading_pos)
        self._renderer.render_button(button)
        self.render_leaderboard()
        self._renderer.update_screen()

    def render_leaderboard(self):
        leaderboard = self._leaderboard.get_leaderboard()
        font_styles = self._leaderboard.get_font_styles()
        headers = self._leaderboard.get_headers()
        self._renderer.render_leaderboard(leaderboard, font_styles, headers)


    def game_over(self, mouse_pos=None):
        button = self._end_screen._button
        if mouse_pos:
            if button.x <= mouse_pos[0] <= button.x + button.width and button.y <= mouse_pos[1] <= button.y + button.height:
                self.game_state = "PLAYING"
        heading = self._end_screen.heading_text()
        heading_pos = self._end_screen._heading_pos
        self._renderer.render_blank_screen()
        self._renderer.render_text(heading, heading_pos)
        self.render_leaderboard()
        self._renderer.render_button(button)
        self._renderer.update_screen()

    def game_loop(self):

        if self._level.game_over():
            self.game_state = "GAME OVER"
        self._level.delete_old_blocks()
        self._level.create_blocks()
        self._level.move_sprites()
        self._level.count_score()
        score = self._level.get_score()
        self._renderer.render_game_screen(score)
        self._renderer.update_screen()
        self._level.adjust_camera()

pygame.quit()
