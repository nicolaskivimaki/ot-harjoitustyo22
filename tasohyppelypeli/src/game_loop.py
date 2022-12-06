import sys
import pygame

class GameLoop:
    def __init__(self, level, renderer, event_queue, clock):
        self._level = level
        self._renderer = renderer
        self._event_queue = event_queue
        self._clock = clock

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    break
            self._level.delete_old_blocks()
            self._level.create_blocks()
            self._level.move_sprites()
            self._level.count_score()
            score = self._level.get_score()
            self._renderer.render(score)
            self._level.adjust_camera()
            self._clock.tick(60)

pygame.quit()
