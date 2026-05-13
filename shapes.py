import pygame

# placeholder for complex or random shapes in the future

"""
class SoftCornerRect:
    def __init__(self, xy, size, border_radius = 1) -> None:
        self.rect = pygame.Rect(xy, size)
        self.border_radius = border_radius
        pass

    def draw(self, surface, color):
        x, y, width, height = self.rect
        br = self.border_radius
        pygame.draw.rect(surface, color, self.rect, 0, br)
        # first rect 
        pygame.draw.rect(surface, color, (x+br, y, width - br*2, height))
        # second rect
        pygame.draw.rect(surface, color, (x, y+br, width, height - br*2))
        # first circle
        pygame.draw.circle(surface, color, (x+br, y+br), br)
        # second
        pygame.draw.circle(surface, color, (x+width-br, y+br), br)
        # third
        pygame.draw.circle(surface, color, (x+width-br, y+height-br), br)
        # fourth
        pygame.draw.circle(surface, color, (x+br, y+height-br), br)"""
        
