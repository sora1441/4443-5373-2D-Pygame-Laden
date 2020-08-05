"""
Brent Laden
Project 1
got assistance with pygame_helper code
video link: https://youtu.be/svt2PuSM74Y
input:
python game.py 600 600 waterbender 
"""
from pygame_helper import *
import math 
import random
import time
import os
import sys

#put command line input int variables
width = int(sys.argv[1],10)
height = int(sys.argv[2],10)
title = sys.argv[3]

#set screen size, color, image, and window title
screenSize = (width,height)
setWindowTitle = title
#setBackgroundColour("black")
setBackgroundImage('background.png')

#set sprites into variables and insert the hoard_no of frames of the sprite
bender = makeSprite('bender.png', 16)
bubble = makeSprite('bubbles.png', 4)
popped = makeSprite('pop.png', 6)
dead = makeSprite('death.png')
zombie = makeSprite('zombies.png', 12)
top_boarder = makeSprite('hortizontal_boarder.png')
bottom_boarder = makeSprite('horizontal_boarder.png')
right_boarder = makeSprite('vertical_boarder.png')
left_boarder = makeSprite('vertical_boarder.png')
bubble.x = 200
bubble.y = 200
moveSprite(zombie, width // 2, height // 2,1)

top_boarder.x = -width
top_boarder.y = 0
bottom_boarder.x = -width
bottom_boarder.y = 2000
right_boarder.x = 2000
right_boarder.y = 50
left_boarder.x = -width
left_boarder.y = 50

moveSprite(top_boarder, top_boarder.x, top_boarder.y)
moveSprite(bottom_boarder, bottom_boarder.x, bottom_boarder.y)
moveSprite(right_boarder, right_boarder.x, right_boarder.y)
moveSprite(left_boarder, left_boarder.x, left_boarder.y)

showSprite(top_boarder)
showSprite(bottom_boarder)
showSprite(right_boarder)
showSprite(left_boarder)

#enemy creation
undead = []
hoard_no = int(sys.argv[5])
#creates undead and adds them to the list
for x in range(hoard_no):
    curr_zombie = makeSprite("zombies.png",12)
    curr_zombie.x = random.randint(0,1000)
    curr_zombie.y = random.randint(0,750)
    curr_zombie.alive = True
    curr_zombie.counter = 0
    moveSprite(curr_zombie, curr_zombie.x, curr_zombie.y)
    curr_zombie.x_speed = 1
    curr_zombie.y_speed = 1
    showSprite(curr_zombie)
    undead.append(curr_zombie)

changeSpriteImage(bubble,2)
showSprite(bender)
moveSprite(bender,width // 2, height // 2, 1)



def main():
    glob_x = 200     #x marker
    glob_y = 200 
    boarder = False         #bool to determine if bender hit boarder
    bubble_direct = "None"  #direction of where bubble should go
    frame=0                 #frame number
    shooting = False        #bool to lock the shoot button, if true you cannot shoot
    nextFrame = clock()     #keeps time of frame changes
    temp_x = 300             #temp location for when you stop moving horizontally
    temp_y = 300             #temp location for when you stop moving vertically
    while True:
        if clock() > nextFrame:     # change frame every 80ms.
            frame = (frame+1)%8     
            nextFrame += 80         
        boarder = False
        #checks to see if we need to print a boarder message
        if temp_x >= 480:
            boarder = True
        if temp_y == 135:
            boarder = True
        if temp_y == 500:
            boarder = True
        if temp_x == 75:
            boarder = True
        if not boarder:
            hideSprite(dead)
            showSprite(bender)
        else:
            hideSprite(bender)
            showSprite(dead)

        #Directional events
            #tracks the logic for when close to barriers to stop scrolling and then start moving the character
        if keyPressed("right"):
            if keyPressed('space'):
                shooting = not shooting     #inverts shooting
                bubble.x = temp_x - 50      #lines up bubble with character
                bubble.y = temp_y - 50
                moveSprite(bubble,bubble.x,bubble.y)
                rotateSprite(bubble,90)
                hideSprite(popped)
                showSprite(bubble)
            if not shooting:
                shooting = True
                bubble_direct = "right"
            if glob_x < 2675 and temp_x == 300:
                top_boarder.x -= 5
                right_boarder.x -= 5
                left_boarder.x -= 5
                bottom_boarder.x -= 5
                moveSprite(top_boarder,top_boarder.x,top_boarder.y)
                moveSprite(right_boarder,right_boarder.x,right_boarder.y)
                moveSprite(left_boarder,left_boarder.x,left_boarder.y)
                moveSprite(bottom_boarder,bottom_boarder.x,bottom_boarder.y)
                glob_x += 5
                scrollBackground(-5,0)  
                for curr_zombie in undead:
                    curr_zombie.x -= 5
                changeSpriteImage(bender, 0*4+frame)
            if glob_x >= 2675 and temp_x <= 480:
                temp_x += 5
                changeSpriteImage(bender, 0*4+frame)
                moveSprite(bender,temp_x,temp_y,1)
                moveSprite(dead,temp_x,temp_y,1)
            elif glob_x <= -80 and temp_x < 300:
                temp_x += 5
                changeSpriteImage(bender, 0*4+frame)
                moveSprite(bender,temp_x,temp_y,1)
                moveSprite(dead,temp_x,temp_y,1)

        elif keyPressed("down"):
            if keyPressed('space'):
                shooting = not shooting
                bubble.x = temp_x - 50
                bubble.y = temp_y - 50
                moveSprite(bubble,bubble.x,bubble.y)
                rotateSprite(bubble,180)
                hideSprite(popped)
                showSprite(bubble)
            if not shooting:
                shooting = True
                bubble_direct = "down"
            if glob_y < 3240 and temp_y == 300:
                top_boarder.y -= 5
                right_boarder.y -= 5
                left_boarder.y -= 5
                bottom_boarder.y -= 5
                moveSprite(top_boarder,top_boarder.x,top_boarder.y)
                moveSprite(right_boarder,right_boarder.x,right_boarder.y)
                moveSprite(left_boarder,left_boarder.x,left_boarder.y)
                moveSprite(bottom_boarder,bottom_boarder.x,bottom_boarder.y)
                glob_y += 5
                scrollBackground(0, -5)
                for curr_zombie in undead:
                    curr_zombie.y -= 5
                changeSpriteImage(bender, 1*4+frame)
            if glob_y >= 3240 and temp_y >=300 and temp_y < 500:
                temp_y += 5
                changeSpriteImage(bender, 1*4+frame)
                moveSprite(bender,temp_x,temp_y,1)
                moveSprite(dead,temp_x,temp_y,1)
            elif glob_y <= 0 and temp_y < 300:
                temp_y += 5
                changeSpriteImage(bender, 1*4+frame)
                moveSprite(bender,temp_x,temp_y,1)
                moveSprite(dead,temp_x,temp_y,1)

        elif keyPressed("left"):
            if keyPressed('space'):
                shooting = not shooting
                bubble.x = temp_x - 50
                bubble.y = temp_y - 50
                moveSprite(bubble,bubble.x,bubble.y)
                rotateSprite(bubble,-90)
                hideSprite(popped)
                showSprite(bubble)
            if not shooting:
                shooting = True
                bubble_direct = "left"
            if glob_x > -435 and temp_x == 300:
                top_boarder.x += 5
                right_boarder.x += 5
                left_boarder.x += 5
                bottom_boarder.x += 5
                moveSprite(top_boarder,top_boarder.x,top_boarder.y)
                moveSprite(right_boarder,right_boarder.x,right_boarder.y)
                moveSprite(left_boarder,left_boarder.x,left_boarder.y)
                moveSprite(bottom_boarder,bottom_boarder.x,bottom_boarder.y)
                glob_x -= 5
                scrollBackground(5,0)
                for curr_zombie in undead:
                    curr_zombie.x += 5
                changeSpriteImage(bender, 2*4+frame)
            if glob_x >= 2675 and temp_x > 300:
                temp_x -= 5
                changeSpriteImage(bender, 2*4+frame)
                moveSprite(bender,temp_x,temp_y,1)
                moveSprite(dead,temp_x,temp_y,1)
            elif glob_x == -435 and temp_x >= 80:
                temp_x -= 5
                changeSpriteImage(bender, 2*4+frame)
                moveSprite(bender,temp_x,temp_y,1)
                moveSprite(dead,temp_x,temp_y,1)

        elif keyPressed("up"):
            if keyPressed('space'):
                shooting = not shooting
                bubble.x = temp_x - 50
                bubble.y = temp_y - 50
                moveSprite(popped,bubble.x,bubble.y)
                hideSprite(bubble)
                showSprite(popped)
            if not shooting:
                shooting = True
                bubble_direct = "up"
            if glob_y > 0 and temp_y == 300:
                top_boarder.y += 5
                right_boarder.y += 5
                left_boarder.y += 5
                bottom_boarder.y += 5
                moveSprite(top_boarder,top_boarder.x,top_boarder.y)
                moveSprite(right_boarder,right_boarder.x,right_boarder.y)
                moveSprite(left_boarder,left_boarder.x,left_boarder.y)
                moveSprite(bottom_boarder,bottom_boarder.x,bottom_boarder.y)
                glob_y -= 5
                scrollBackground(0,5)
                for curr_zombie in undead:
                    curr_zombie.y += 5
                changeSpriteImage(bender,3*4+frame)
            if glob_y >= 3240 and temp_y >= 300:
                temp_y -=5
                changeSpriteImage(bender,3*4+frame)
                moveSprite(bender,temp_x,temp_y,1)
                moveSprite(dead,temp_x,temp_y,1)
            elif glob_y <= 0 and temp_y >= 140:
                temp_y -=5
                changeSpriteImage(bender,3*4+frame)
                moveSprite(bender,temp_x,temp_y,1)
                moveSprite(dead,temp_x,temp_y,1)
        else:
            changeSpriteImage(bender, 5)
            changeSpriteImage(dead,frame%1)

        #updates the bubble location for each frame and sets it in the right direction
        if bubble.x == 250 and bubble.y == 250:
            time.sleep(.05)
        if bubble_direct == "right":
            bubble.x += 5
        elif bubble_direct == "left":
            bubble.x -= 5
        elif bubble_direct == "up":
            bubble.y -= 5
        elif bubble_direct == "down":
            bubble.y += 5

        #collision check
        logic_bool = 0
        for curr_zombie in undead:
            if curr_zombie.alive == False:
                curr_zombie.counter += 1
                if curr_zombie.counter >= 200:
                    hideSprite(curr_zombie)
            if logic_bool == 0 and curr_zombie.alive == True:
                curr_zombie.x += curr_zombie.xspeed
                if curr_zombie.x > 1000:
                    curr_zombie.x = 0
                elif curr_zombie.x < 0:
                    curr_zombie.x = 1000
                changeSpriteImage(curr_zombie,(frame%4))
                moveSprite(curr_zombie, curr_zombie.x, curr_zombie.y)
            if logic_bool == 1 and curr_zombie.alive == True:
                curr_zombie.y += curr_zombie.yspeed
                if curr_zombie.y > 750:
                    curr_zombie.y = 0
                elif curr_zombie.y < 0:
                    curr_zombie.y = 750
                changeSpriteImage(curr_zombie,frame%4)
                moveSprite(curr_zombie, curr_zombie.x, curr_zombie.y)
            if logic_bool == 0: logic_bool = 1
            else: logic_bool = 0
            if abs(curr_zombie.x - bubble.x) <= 30 and abs(curr_zombie.y - bubble.y) <= 30:
                curr_zombie.alive = False
                changeSpriteImage(curr_zombie,13)
                hideSprite(bubble)
                hideSprite(popped)
            moveSprite(curr_zombie, curr_zombie.x, curr_zombie.y)
                
        changeSpriteImage(bubble,frame%4)
        moveSprite(bubble,bubble.x,bubble.y)
        moveSprite(popped,bubble.x,bubble.y)
        updateDisplay()
        tick(120)

    endWait()

if __name__=='__main__':
    main()