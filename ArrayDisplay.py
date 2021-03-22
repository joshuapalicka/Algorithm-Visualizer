from time import sleep, perf_counter
from SelectionSort import *
import pygame
from pygame.locals import *

import array


class ArrayDisplay:
    def __init__(self, arr, sortNum):

        self.array = arr

        self.length = len(arr)

        if sortNum == 0:
            self.curSort = SelectionSort(self.array, self.length, 1)

        elif sortNum == 1:
            self.curSort = SelectionSort(self.array, self.length, 1)  # fix for other sort

        self.width = 1000
        self.height = 500
        self.size = self.width, self.height

        self.totalRectangles = self.length

        self.fromLeft = 10

        self.startFromTop = (self.height / 2) - 10

        self.vSizeMultiplier = self.height / self.length

        self.black = 0, 0, 0
        self.white = 255, 255, 255

        self.green = 0, 128, 0
        self.red = 255, 0, 0

        self.screen = pygame.display.set_mode(self.size)

        pygame.font.init()

        self.curFont = pygame.font.SysFont("Calibri", 12)

        self.clock = pygame.time.Clock()

        self.startGameLoop()

    def startGameLoop(self):
        white = 255, 255, 255

        screen = pygame.display.set_mode(self.size)
        pygame.init()
        pygame.display.set_caption(self.curSort.getName())

        screen.fill(white)
        pygame.display.flip()

        self.updateBox()

    def scanArray(self):
        for i in range(1, self.length):
            pygame.display.flip()
            self.clock.tick(144)
            textbox = self.curFont.render(
                "Swaps: " + self.curSort.getSwaps() + " Comparisons: " + self.curSort.getComparisons(), False,
                self.black)
            self.array = self.curSort.getArray()
            vRectSize = self.curSort.getArray()[i]
            pygame.draw.line(self.screen, self.green, [i, self.height],
                             [i, self.height - (vRectSize * self.vSizeMultiplier)], 1)
            self.screen.blit(textbox, (0, 0))
        pygame.display.flip()

    def updateBox(self):

        updateBool = True
        while updateBool:
            self.screen.fill(self.white)
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            self.array = self.curSort.getArray()

            for i in range(1, self.length):
                textbox = self.curFont.render(
                    "Swaps: " + self.curSort.getSwaps() + " Comparisons: " + self.curSort.getComparisons(), False,
                    self.black)
                self.array = self.curSort.getArray()
                vRectSize = self.curSort.getArray()[i]
                pygame.draw.line(self.screen, self.black, [i, self.height],
                                 [i, self.height - (vRectSize * self.vSizeMultiplier)], 1)
                self.screen.blit(textbox, (0, 0))

            pygame.display.flip()

            updateBool = self.curSort.update()

        self.scanArray()
        sleep(5)



