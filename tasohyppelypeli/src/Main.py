import pygame
from ui.level import Level
from game_loop import GameLoop
from features.event_que import EventQueue
from features.renderer import Renderer
from features.clock import Clock

def main():

    pygame.init()
    display = pygame.display.set_mode((500, 600))
    display.fill((255, 255, 255))
    pygame.display.set_caption("Tasohyppelypeli")

    level = Level()
    event_queue = EventQueue()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, event_queue, clock)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
