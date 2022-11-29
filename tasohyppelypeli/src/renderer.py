import pygame

class Renderer:
    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render(self):
        self._display.fill((255, 255, 255))
        for block in self._level.blocks:
            block.move_block()
        self._level.robot.handle_keys()
        self._level.robot.robot_jumping()
        self._level.all_sprites.draw(self._display)
        pygame.display.update()
