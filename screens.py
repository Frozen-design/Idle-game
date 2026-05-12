import pygame
from buttons import *
from managers import *

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
        self.event_checks = [self.exit_check]
        self.active = True
    
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
                for funct in self.event_checks:
                    new_screen = funct(event)
                    if new_screen:
                        self.active = False
            self.update()
            self.window.flip()
            self.window.clock.tick(60)
        return new_screen

class MainMenu(Screen):
    def __init__(self, manager, window: Window):
        super().__init__(manager, window)
        self.event_checks.append(self.switch_to_game) # type: ignore

    def update(self):
        self.window.surface.fill("dark blue")

    def switch_to_game(self, event:pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONUP:
            return GameScreen

class GameScreen(Screen):
    def __init__(self, manager, window: Window):
        super().__init__(manager, window)
        
    def setup(self):
        self.event_checks.append(self.increment_click) # type: ignore
        self.rs_manager = ResourceManager()
        rsm_info = {"rs_manager": self.rs_manager}
        wood_button_colors = {"inner_color": pygame.Color(103, 68, 34), "outer_color": "brown", "text_color": "white"}
        self.first_button = StylizedButton((100, 100), (100, 40), text = "Chop Wood", **wood_button_colors, **rsm_info, rs_name = "wood")
        self.worker_button = StylizedButton((100, 200), (100, 40), text = "Worker", **rsm_info, rs_name = "loggers")
        self.event_checks.append(self.first_button.click_event)
        self.event_checks.append(self.worker_button.click_event)

    def update(self):
        self.window.surface.fill("dark grey")
        self.first_button.draw(self.window.surface)
        self.first_button.draw_value(self.window.surface)
        self.worker_button.draw(self.window.surface)
        self.worker_button.draw_value(self.window.surface)

    def increment_click(self, event:pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.first_button.check_click(event.pos)