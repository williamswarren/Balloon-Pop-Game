import pygame
from pygame.locals import *
import random

# BALL CLASS 
class Drop():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.dropImage = pygame.image.load("images/pin.png")
        # A rect is made up of [x, y, width, height]
        dropRect = self.dropImage.get_rect()
        self.width = dropRect[2]
        self.height = dropRect[3]
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        
        # Pick a random starting position for x
        self.x = random.randrange(0, self.maxWidth)
        self.y = 0

        # store area of object to see if drop collides with ball
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)

        # Choose a random speed for y direction      
        self.ySpeed = random.randrange(1, 4)

    def update(self):
        # check for hitting bottom wall. If so, restart the drop

        if self.y > self.maxHeight:
            self.x = random.randrange(0,self.maxWidth)
            self.y = 0
            self.ySpeed = random.randrange(1,4)

        # update the drop position
        self.y = self.y + self.ySpeed

        # update area
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.window.blit(self.dropImage, (self.x, self.y))