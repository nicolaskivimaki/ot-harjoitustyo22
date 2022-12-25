import pygame
from button import Button

class EndScreen():

    def __init__(self):

        self._heading_pos = (125, 60)
        self._score_pos = (190, 135)
        self._button = Button(190, 180, 130, 40, "PLAY AGAIN", font="arial", font_size=16,
                 font_color=(0, 0, 0), background_color=(255, 255, 255),
                 border_color=(0, 0, 0), border_width=4)

    def heading_text(self):

        heading = "GAME OVER"
        colour = (0, 0, 0)
        font = pygame.font.SysFont("arial black", 38)
        text = font.render(heading, True, colour)
        return text

    def score_text(self, score):

        score_text = f"Your score: {score}"
        colour = (0, 0, 0)
        font = pygame.font.SysFont("arial ", 20)
        text = font.render(score_text, True, colour)
        return text
        