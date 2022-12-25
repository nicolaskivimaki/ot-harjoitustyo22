class Button:
    def __init__(self, x, y, width, height, text=None, font=None, font_size=36,
                 font_color=(0, 0, 0), background_color=(255, 255, 255),
                 border_color=(0, 0, 0), border_width=2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.background_color = background_color
        self.border_color = border_color
        self.border_width = border_width
