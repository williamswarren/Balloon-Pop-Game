import pygame
from pygame.locals import *

class Score():
    def __init__(self, window):
        self.window = window
        self.x = 0
        self.y = -15
        self.ones = "0"
        self.tens = "0"
        self.hundreds = "0"
        self.thousands = "0"
        self.current_score = "0"
        self.high_score = "0"
        self.points = pygame.image.load("images/Points.png")
        self.highscore = pygame.image.load("images/Highscore.png")
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

    def update(self, len_ball_list, len_drop_list):
        if len_ball_list == 0:
            if int(self.current_score) > int(self.high_score): #Update high score
                self.high_score = self.current_score
                
            #Reset Score to 0
            self.ones = "0"
            self.tens = "0"
            self.hundreds = "0"
            self.thousands = "0"
            self.current_score = "0"

        else:
            #Update score to take into account amount of Balloons, Time, & amount of Tacks
            self.current_score = str(int(self.current_score) + (1 * len_ball_list * len_drop_list))
            for index in range(-1, -len(self.current_score)-1, -1):
                if index == -1:
                    self.ones = self.current_score[index]
                elif index == -2:
                    self.tens = self.current_score[index]
                elif index == -3:
                    self.hundreds = self.current_score[index]
                elif index == -4:
                    self.thousands = self.current_score[index]

    def draw(self):
        #Points
        self.window.blit(self.points, (self.x, self.y))
        self.window.blit(self.numbers[self.ones],(self.x + 135, self.y + 22))
        self.window.blit(self.numbers[self.tens],(self.x + 120, self.y + 22))
        self.window.blit(self.numbers[self.hundreds],(self.x + 105, self.y + 22))
        self.window.blit(self.numbers[self.thousands],(self.x + 90, self.y + 22))
        #HighScore
        self.window.blit(self.highscore, (self.x, self.y + 50))
        for index in range(-1, -(len(self.high_score))-1, -1):
            if index == -1:
                self.window.blit(self.numbers[self.high_score[index]], (self.x + 60, self.y + 100))
            elif index == -2:
                self.window.blit(self.numbers[self.high_score[index]], (self.x + 45, self.y + 100))
            elif index == -3:
                self.window.blit(self.numbers[self.high_score[index]], (self.x + 30, self.y + 100))
            elif index == -4:
                self.window.blit(self.numbers[self.high_score[index]], (self.x + 15, self.y + 100))



        #draw high score
        #self.window.blit(self.numbers[self.high_score], (self.x + 160, self.y + 72))
