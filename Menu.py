import pygame
import random
from pygame_menu import Theme
from pygame_menu.themes import THEME_DARK

from ArrayDisplay import *
import pygame_menu
from array import *

def randomArrayGen(length):
    randList = list(range(length))
    random.shuffle(randList)
    arr = array('i')
    arr.fromlist(randList)
    return arr


class Menu:
    def __init__(self):
        self.length = 100
        self.sortNum = 0
        pygame.init()
        self.width = 600
        self.height = 400
        self.createMenu(self.width, self.height)

    def createMenu(self, width, height):
        sortItems = ['Selection Sort', 'Bubble Sort', 'Insertion Sort']

        curTheme = Theme(background_color=(40, 41, 35),
                         cursor_color=(255, 255, 255),
                         cursor_selection_color=(80, 80, 80, 120),
                         scrollbar_color=(39, 41, 42),
                         scrollbar_slider_color=(65, 66, 67),
                         scrollbar_slider_hover_color=(90, 89, 88),
                         selection_color=(255, 255, 255),
                         title_background_color=(47, 48, 51),
                         title_font_color=(215, 215, 215),
                         widget_font_color=(200, 200, 200)
                         )
        curTheme.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_UNDERLINE
        # curTheme.title_bar_style = pygame_menu.locals

        surface = pygame.display.set_mode((width, height), RESIZABLE)
        menu = pygame_menu.Menu('Algorithm Visualizer', width, height, theme=curTheme)

        menu.add.text_input('Array Size: ', default=100, onchange=self.setSize)
        menu.add.dropselect('Sorting Algorithm: ', sortItems, onreturn=self.selectSort)
        menu.add.button('Start', self.createArrayDisplay)

        while True:
            events = pygame.event.get()
            for event in events:

                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.WINDOWSIZECHANGED:
                    screenSize = pygame.display.get_surface().get_size()
                    width, height = screenSize
                    self.createMenu(width, height)

            if menu.is_enabled():
                menu.update(events)
                menu.draw(surface)

            pygame.display.update()

    def setSize(self, size):
        self.length = int(size)
        pass

    def selectSort(self, num):
        self.sortNum = num
        pass

    def createArrayDisplay(self):
        arr = array('i', randomArrayGen(self.length))
        display = ArrayDisplay(arr, self.sortNum)
