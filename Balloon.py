import pygame
from pygame.locals import *
import random

# BALL CLASS 
class Balloon():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # remember the window, so we can draw later
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        
        self.clicked = False # if we need to custom draw or handle regular wall collide
        self.collide = False

        self.balloonImage = pygame.image.load("images/balloon.png")
        self.popSound = pygame.mixer.Sound("sounds/blop.wav")
        self.popImage = pygame.image.load("images/smoke.png")
        # A rect is made up of [x, y, width, height]
        balloonRect = self.balloonImage.get_rect()
        self.width = balloonRect[2]
        self.height = balloonRect[3]
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height
        
        # Pick a random starting position 
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # store area of object to see if mouse collides
        self.area = pygame.Rect(self.x, self.y, self.width, self.height)

        # Choose a random speed in both the x and y directions
        self.xSpeed = random.randrange(-3, 4)       
        self.ySpeed = random.randrange(-3, 4)

        # Make sure neither are 0

        if self.xSpeed == 0:
            self.xSpeed += 1
        
        if self.ySpeed == 0:
            self.ySpeed -= 1

    def checkClick(self, mouse_pos):
        if self.area.collidepoint(mouse_pos):
            self.clicked = True

    def checkCollide(self, drop):
        if self.area.colliderect(drop.area):
                self.collide = True

    def update(self, mouse_event):
        if mouse_event == "clicked":
            # change direction of speeds
            self.xSpeed = -self.xSpeed
            self.ySpeed = -self.ySpeed

            # update the balls x and y, based on the speed in two directions
            self.x = self.x + self.xSpeed
            self.y = self.y + self.ySpeed

            # update area
            self.area = pygame.Rect(self.x, self.y, self.width, self.height)

            # allow to be clicked again by user
            self.clicked = False

        else:
            # check for hitting a wall.  If so, change that direction
            if (self.x < 0) or (self.x > self.maxWidth):
                self.xSpeed = -self.xSpeed

            if (self.y < 0) or (self.y > self.maxHeight):
                self.ySpeed = -self.ySpeed

            # update the balls x and y, based on the speed in two directions
            self.x = self.x + self.xSpeed
            self.y = self.y + self.ySpeed

            # update area
            self.area = pygame.Rect(self.x, self.y, self.width, self.height)


    def draw(self, action):
        if action == "destroy":
            self.popSound.play()
            self.window.blit(self.popImage, (self.x, self.y))
        else:
            self.window.blit(self.balloonImage, (self.x, self.y))

    def __del__(self):
        del self
