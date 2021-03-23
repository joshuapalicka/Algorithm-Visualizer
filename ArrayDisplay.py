from time import sleep, perf_counter, perf_counter_ns
from SelectionSort import *
from BubbleSort import *
from InsertionSort import *
import pygame
from pygame.locals import *
import os

import array


def getColor(LRBool, RLBool): # returns green if bool is true and red if false
    if LRBool or RLBool:
        return 0, 128, 0
    return 255, 0, 0


class ArrayDisplay:
    def __init__(self, arr, sortNum):
        self.array = arr

        self.length = len(arr)

        if sortNum == 0:
            self.curSort = SelectionSort(self.array)

        elif sortNum == 1:
            self.curSort = BubbleSort(self.array)  # fix for other sort

        elif sortNum == 2:
            self.curSort = InsertionSort(self.array)

        self.width = self.length * 3
        self.height = 800
        self.size = self.width, self.height

        self.startFromTop = (self.height / 2) - 10

        self.vSizeMultiplier = self.height / self.length

        self.black = 0, 0, 0
        self.white = 255, 255, 255

        self.green = 0, 128, 0
        self.red = 255, 0, 0

        self.screen = pygame.display.set_mode(self.size)

        pygame.font.init()

        self.curFont = pygame.font.SysFont("Calibri", 20)

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

    def updateBox(self):
        gray = 50, 50, 50

        updateBool = True

        avgTime = 0
        totalTime = 0

        while updateBool:
            sortedLRBool = True
            sortedRLBool = True
            self.screen.fill(gray)
            self.clock.tick(144)

            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            self.array = self.curSort.getArray()

            for i in range(0, self.length):
                textbox = self.curFont.render(
                    "Swaps: " + self.curSort.getSwaps() + " Comparisons: " + self.curSort.getComparisons() +
                    " Nanoseconds Per Item: " + str(avgTime), False, self.white)

                if i != self.length-1:
                    if self.array[i] != self.array[i+1] - 1:
                        sortedLRBool = False
                if i != 0:
                    if self.array[(self.length-1) - i] != self.array[i-1] + 1:
                        sortedRLBool = False

                vRectSize = self.array[i]
                pygame.draw.line(self.screen, getColor(sortedLRBool, sortedRLBool), [i*3, self.height],
                                 [i*3, self.height - (vRectSize * self.vSizeMultiplier)], 2)
                self.screen.blit(textbox, (0, 0))

            pygame.display.flip()

            beginUpdateTime = perf_counter_ns()
            updateBool = self.curSort.update()
            endUpdateTime = perf_counter_ns()

            totalTime += (endUpdateTime - beginUpdateTime)
            avgTime = totalTime / (self.curSort.getCurI() + 1)

        sleep(5)



