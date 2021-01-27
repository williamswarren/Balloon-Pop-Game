import time
import math
import pygame
from pygame.locals import *

class Time():
    def __init__(self, window, windowWidth, windowHeigh):
        self.window = window
        self.x = windowWidth - 100
        self.y = 10
        self.start_time = time.time()
        self.current_time = "0"
        self.ones = "0"
        self.tens = "0"
        self.hundreds = "0"
        self.thousands = "0"
        self.clock = pygame.image.load("images/Digital-Clock.png")
        self.numbers = {"0":pygame.image.load("images/zero.png"), 
                        "1":pygame.image.load("images/one.png"), 
                        "2":pygame.image.load("images/two.png"), 
                        "3":pygame.image.load("images/three.png"), 
                        "4":pygame.image.load("images/four.png"), 
                        "5":pygame.image.load("images/five.png"), 
                        "6":pygame.image.load("images/six.png"),
                        "7":pygame.image.load("images/seven.png"), 
                        "8":pygame.image.load("images/eight.png"), 
                        "9":pygame.image.load("images/nine.png")}
    
    def update(self):
        #Get the current time
        self.current_time = str(int(time.time() - self.start_time))
        if int(self.current_time) < 60: #Handle seconds up to 1 minute
            for index in range(-1, -len(self.current_time)-1, -1): 

                if index == -1:
                    self.ones = self.current_time[index]
                if index == -2:
                    self.tens = self.current_time[index]

        if int(self.current_time) >= 60: #Handle time over 60 seconds
            self.hundreds = str(math.floor(int(self.current_time)/60))
            ones_tens = str(int(self.current_time)%60)
            if ones_tens == "0":
                self.ones = "0"
                self.tens = "0"
            else:
            # iterate through remaining seconds and update clock
                for index in range(-1, -len(ones_tens)-1, -1):
                    if index == -1:
                        self.ones = ones_tens[index]
                    if index == -2:
                        self.tens = ones_tens[index]



    def draw(self):
        self.window.blit(self.clock, (self.x, self.y))
        self.window.blit(self.numbers[self.thousands], (self.x + 5, self.y + 8))
        self.window.blit(self.numbers[self.hundreds], (self.x + 20, self.y + 8))
        self.window.blit(self.numbers[self.tens], (self.x + 45, self.y + 8))
        self.window.blit(self.numbers[self.ones], (self.x + 60, self.y + 8))


