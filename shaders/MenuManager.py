import pygame as pg


class MenuManager(object):
    def __init__(self):
        self.states = (
            'MainMenu',
            'Game'
        )
        self.current_state = 'Game'

    def update(self, core):
        if self.current_state == 'MainMenu':
            pass
        if self.current_state == 'Game':
            core.get_map().update(core)

    def render(self, core):
        if self.current_state == 'MainMenu':
            pass
        if self.current_state == 'Game':
            core.get_map().render(core)

        pg.display.update()
