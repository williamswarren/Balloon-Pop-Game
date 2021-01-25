# pygame demo using Ball class, bounce many balls

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Balloon import *  # bring in the Ball class code
from Drop import * # bring in Drop class node
from Time import * # bring in Time class
from Score import *

# 2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
#N_BALLS = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)
timer = Time(window, WINDOW_WIDTH, WINDOW_HEIGHT)
points = Score(window)
print("Current time is: ", timer.current_time)

# 4 - Load assets: image(s), sounds, etc.
oInstructions = pygame.image.load('images/instructions.png')

# 5 - Initialize variables
balloonList = []
dropList = []
#for oBall in range(0, N_BALLS):
    # create a ball object for each ball
    #oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    #ballList.append(oBall)  # append the new ball to the list of balls   

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # This is kind of strange, where if I remove event.type and go straight to event.key I get thrown an error "Event does not contain attribute Key"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                oBalloon = Balloon(window, WINDOW_WIDTH, WINDOW_HEIGHT)
                balloonList.append(oBalloon)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                oDrop = Drop(window, WINDOW_WIDTH, WINDOW_HEIGHT)
                dropList.append(oDrop)

        # Check if mouse down is inside the ball objects rect
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for balloonObject in balloonList:
                balloonObject.checkClick(mouse_pos)
                #if balloonObject.area.collidepoint(mouse_pos):
                    #balloonObject.clicked = True

    # Check if collision between balloon and drop
    if dropList and balloonList:
        for obal in balloonList:
            for odrop in dropList:
                #print(obal.__dict__)
                #print(odrop.__dict__)
                obal.checkCollide(odrop)
                #if obal.area.colliderect(odrop.area):
                    #obal.collide = True

    # 8 - Do any "per frame" actions
    for oBalloon in balloonList:
        if oBalloon.clicked:
            oBalloon.update("clicked")
            #oBalloon.clicked = False
        else:
            oBalloon.update("not-clicked")  # tell each ball to update itself
    
    for oDrop in dropList:
        oDrop.update()


    timer.update() # update game clock time

    points.update(len(balloonList), len(dropList)) # update points
    
   # 9 - Clear the screen before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the screen elements
    window.blit(oInstructions, (85, 430))
    points.draw() 
    timer.draw()
    print("Current time is: ", timer.current_time)
    balloon_list_length = len(balloonList)
    index = 0
    while index < balloon_list_length:
        if not balloonList[index].collide:
            balloonList[index].draw("regular")   # tell each ball to draw itself normally
            index += 1
        else:
            balloonList[index].draw("destroy") # tell the ball to draw the air to the screen
            del balloonList[index] # remove balloon from list (this does not seem like the right way to dereference/destructure it...)
            balloon_list_length -= 1
            

    for oDrop in dropList:
        oDrop.draw() # tell each drop to draw itself

       
    # 11 - Update the screen
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make PyGame wait the correct amount


