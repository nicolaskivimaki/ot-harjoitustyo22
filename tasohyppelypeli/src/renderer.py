import pygame

class Renderer:

    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self, score):

        self._display.fill((255, 255, 255))
        self._level.all_sprites.draw(self._display)
        self._level.robot_group.draw(self._display)
        self.render_score_text(score)
        pygame.display.update()

    def render_score_text(self, score):

        score_text = f"SCORE: {score}"
        colour = (0, 0, 0)
        position = (390, 2)
        font = pygame.font.SysFont("arial black", 16)
        text = font.render(score_text, True, colour)
        self._display.blit(text, (position))
