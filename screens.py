import pygame
from buttons import *
from managers import *
from shapes import *

class Window:
    def __init__(self, width, height):
        pygame.init()
        pygame.font.init()
        self.width, self.height = width, height
        self.surface = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def flip(self):
        pygame.display.flip()

class ScreenManager:
    def __init__(self, window) -> None:
        self.window = window
        self.stage = MainMenu(self, window)

    def run_current_screen(self):
        return_value = self.stage.run()
        if return_value:
            self.stage = return_value(self, self.window)
            self.run_current_screen()

class Screen:
    def __init__(self, manager:ScreenManager, window: Window):
        self.manager = manager
        self.window = window
        self.surface = window.surface
        self.active = True

    def check_events(self, event):
        pass
    
    def exit_check(self, event):
        if event.type == pygame.QUIT:
            self.active = False
            return None

    def update(self):
        self.window.surface.fill("black")
        pass

    def setup(self):
        pass

    def run(self):
        self.active = True
        new_screen = None
        self.setup()
        while self.active:
            for event in pygame.event.get():
                self.exit_check(event)
                new_screen = self.check_events(event)
                if new_screen:
                    self.active = False
            self.update()
            self.window.flip()
            self.window.clock.tick(60)
        return new_screen

class MainMenu(Screen):
    def __init__(self, manager, window: Window):
        super().__init__(manager, window)

    def update(self):
        self.window.surface.fill("dark blue")

    def check_events(self, event): # type: ignore
        switch_event = self.switch_to_game(event)
        if switch_event != None:
            return switch_event

    def switch_to_game(self, event:pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONUP:
            return GameScreen

class GameScreen(Screen):
    def __init__(self, manager, window: Window):
        super().__init__(manager, window)
        
    def setup(self):
        self.rs_manager = ResourceManager()
        rsm_info = {"rs_manager": self.rs_manager}
        wood_button_colors = {"inner_color": pygame.Color(103, 68, 34), "outer_color": "brown", "text_color": "white"}
        self.wood_button    = StylizedButton((100, 100), (100, 40)   , text = "Chop Wood", rs_name = "wood"   , **wood_button_colors, **rsm_info)
        self.logger_button  = StylizedButton((100, 200), (100, 40)   , text = "Loggers"  , rs_name = "loggers", **rsm_info)

    def check_events(self, event):
        self.wood_button.click_event(event)
        self.logger_button.click_event(event)

    def update(self):
        self.window.surface.fill("dark grey")
        self.wood_button.draw(self.surface)
        self.wood_button.draw_value(self.surface)
        self.logger_button.draw(self.surface)
        self.logger_button.draw_value(self.surface)