import pygame

class Button:
    def __init__(self, xy, size, color):
        self.rect = pygame.Rect((xy, size))
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def check_click(self, xy):
        return self.rect.collidepoint(xy)
    
class VarButton:
    def __init__(self, button:Button, name, desc):
        self.button = button
        self.name = name
        self.value = 0
        self.description = desc

    def check_click(self, xy):
        if self.button.check_click(xy):
            self.value += 1

    def draw(self, surface:pygame.Surface):
        self.button.draw(surface)
        rect = self.button.rect
        font = pygame.font.Font(None, size = 20)
        font_surf = font.render(self.name, True, "White")
        font_rect = font_surf.get_rect(center = rect.center)
        surface.blit(font_surf, font_rect)

    def draw_value(self, surface):
        rect = self.button.rect
        font = pygame.font.Font(None, size = 20)
        font_surf = font.render(str(self.value), True, "Black")
        font_rect = font_surf.get_rect(center = [a + b for a, b in zip(rect.center, [0, -rect.height])])
        surface.blit(font_surf, font_rect)
