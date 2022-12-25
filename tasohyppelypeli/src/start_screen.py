import pygame
from button import Button

class StartScreen():

    def __init__(self):
        self._heading_pos = (135, 60)
        self._button = Button(190, 150, 130, 40, "START GAME", font="arial", font_size=16,
                 font_color=(0, 0, 0), background_color=(255, 255, 255),
                 border_color=(0, 0, 0), border_width=4)

    def heading_text(self):

        heading = "ROBOJUMP"
        colour = (0, 0, 0)
        font = pygame.font.SysFont("arial black", 38)
        text = font.render(heading, True, colour)
        return text


        