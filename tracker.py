import pygame

class Tracker:
    def __init__(self, window, rs_manager) -> None:
        self.window = window
        self.screen = self.window.surface # type: pygame.Surface
        self.rs_manager = rs_manager
        pass