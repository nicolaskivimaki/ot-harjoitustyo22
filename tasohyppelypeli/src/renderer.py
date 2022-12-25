import pygame

class Renderer:

    def __init__(self, display, level):
        self._display = display
        self._level = level

    def render_text(self, text, position):

        self._display.blit(text, (position))

    def render_blank_screen(self):

        self._display.fill((255, 255, 255))

    def render_leaderboard(self, rows, font_styles, headers):

        i = 20

        column_font = pygame.font.SysFont(font_styles[0], font_styles[1])
        header_font = pygame.font.SysFont(font_styles[2], font_styles[3])
        headfont = pygame.font.SysFont(font_styles[2], 28)


        header = headfont.render('LEADERBOARD', True, (0, 0, 0))
        head1 = header_font.render('PLAYER', True, (0, 0, 0))
        head2 = header_font.render('SCORE', True, (0, 0, 0))
        self._display.blit(header, ((130, 250)))
        self._display.blit(head1, ((120, 310)))
        self._display.blit(head2, ((295, 310)))

        for row in rows:

            name = row['player']
            score = row['score']
            column1 = column_font.render('{:>3}'.format(name), True, (0, 0, 0))
            column2 = column_font.render('{:30}'.format(score), True, (0, 0, 0))
            self._display.blit(column1, ((140, 330 + i)))
            self._display.blit(column2, ((215, 330 + i)))

            i += 20
    

    def render_button(self, button):

        pygame.draw.rect(self._display, button.border_color, (button.x, button.y, button.width, button.height), button.border_width)
        pygame.draw.rect(self._display, button.background_color, (button.x + button.border_width, button.y + button.border_width,
                                                        button.width - 2 * button.border_width, button.height - 2 * button.border_width))
        font = pygame.font.SysFont(button.font, button.font_size)
        text_surface = font.render(button.text, True, button.font_color)
        text_rect = text_surface.get_rect()
        text_rect.center = (button.x + button.width // 2, button.y + button.height // 2)
        self._display.blit(text_surface, text_rect)

    def render_game_screen(self, score):

        self._display.fill((255, 255, 255))
        self._level.all_sprites.draw(self._display)
        self._level.robot_group.draw(self._display)
        self.render_score_text(score)

    def render_score_text(self, score):

        score_text = f"SCORE: {score}"
        colour = (0, 0, 0)
        position = (380, 2)
        font = pygame.font.SysFont("arial black", 20)
        text = font.render(score_text, True, colour)
        self._display.blit(text, (position))

    def update_screen(self):
        pygame.display.update()