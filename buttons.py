import pygame

class Button:
    def __init__(self, xy, size, color):
        self.rect = pygame.Rect((xy, size))
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def check_click(self, xy):
        return self.rect.collidepoint(xy)

class StylizedButton(Button):
    def __init__(self, xy, size, **kwargs):
        self.kwargs = kwargs
        super().__init__(xy, size, kwargs.get("outer_color", "blue"))
        corners = ["left", "top", "right", "bottom"]
        temp_margins = {a: kwargs.get(a, 5) for a in corners}
        self.margins = kwargs.get("margins", temp_margins)
        self.text = kwargs.get("text", "N/A")
        self.text_color = kwargs.get("text_color", "black")
        self.font_name = self.kwargs.get("font_name", "Arial")
        self.rs_manager = kwargs.get("rs_manager", None)
        self.rs_name = kwargs.get("rs_name", None)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=5)
        x, y = self.rect.topleft
        width, height = self.rect.size
        x += self.margins["left"]
        y += self.margins["top"]
        width -= (self.margins["left"] + self.margins["right"])
        height -= (self.margins["top"] + self.margins["bottom"])
        pygame.draw.rect(surface, self.kwargs.get("inner_color", "light blue"), (x, y, width, height), border_radius=5)
        font = pygame.font.SysFont(self.font_name, size = self.kwargs.get("font_size", min((width * 2)//4, (height * 2)//4)))
        font_sfc = font.render(self.text, True, self.text_color)
        surface.blit(font_sfc, font_sfc.get_rect(center = self.rect.center))

    def draw_value(self, surface):
        if self.rs_name and self.rs_manager:
            value = self.rs_manager.get_quantity(self.rs_name)
            if value != None:
                rect = self.rect
                font = pygame.font.SysFont(self.font_name, size = 20)
                font_surf = font.render(str(value), True, "Black")
                font_rect = font_surf.get_rect(midleft = [a + b for a, b in zip(rect.center, [rect.width * 2 // 3, 0])])
                surface.blit(font_surf, font_rect)

    def click_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.check_click(event.pos) and self.rs_manager:
                self.rs_manager.add_quantity(self.rs_name, 1)