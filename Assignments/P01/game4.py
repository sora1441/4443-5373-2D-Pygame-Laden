'''
Brent Laden
Project 1
got assistance with pygame_helper code
video link: https://youtu.be/svt2PuSM74Y
input:
python game.py 600 600 waterbender 
'''
from pygame_helper import *
import math
import random
import time
import os

#command line input variables
width = int(sys.argv[1])
height = int(sys.argv[2])
enemy_no = int(sys.argv[5])
setWindowTitle(sys.argv[3])

#screen size and color
screenSize(width,height)
setBackgroundColour('black')

pos_x = 0
pos_y = 0

setBackgroundImage('bg.png')
bender = makeSprite('bender.png',16)
dead = makeSprite('death.png')
bubbles = makeSprite('bubbles.png',4)
reset_bubble = makeSprite('bubbles.png',4)
top = makeSprite('horizontal_boarder.png')
bottom = makeSprite('horizontal_boarder.png')
right = makeSprite('vertical_boarder.png')
left = makeSprite('vertical_boarder.png')
bubbles.x = 200
bubbles.y = 200
hideSprite(dead)
moveSprite(dead,int(sys.argv[1]) // 2,int(sys.argv[2]) // 2,1)
top.x = -500
top.y = 0
right.x = 3189
right.y = 79
left.x = -500
left.y = 50
bottom.x = -500
bottom.y = 3789
moveSprite(top,top.x,top.y)
moveSprite(right,right.x,right.y)
moveSprite(left,left.x,left.y)
moveSprite(bottom,bottom.x,bottom.y)
showSprite(top)
showSprite(right)
showSprite(left)
showSprite(bottom)

#enemy creation
def_no = 10
zombie_no = []
if enemy_no % 2 != 0:
    def_no = enemy_no + 1
else:
    def_no = enemy_no
for x in range(def_no):
    undead = makeSprite('zombies.png',13)
    showSprite(undead)
    undead.x = random.randint(0,1000)
    undead.y = random.randint(0,750)
    moveSprite(undead, undead.x, undead.y)
    undead.alive = True
    undead.counter = 0
    undead.xspeed = 1
    undead.yspeed = 1

    zombie_no.append(undead)

changeSpriteImage(bubbles,2)
showSprite(bender)
moveSprite(bender,int(sys.argv[1]) // 2,int(sys.argv[2]) // 2,1)

def main():
    global pos_x            #x marker
    global pos_y            #y marker
    tempx = 300
    tempy = 300
    wall_hit = False        #wether player is touching the wall
    quit_moving = False     #wether the player should move
    shooting = False        #wheter player can shoot or not
    bubble_direct = 'None'
    logic_bool = 0           
    nextFrame = clock()
    #playSound('audio.mp3',1) #could not get to work
    frame=0
    blit_no = 0

    while True:
        if clock() > nextFrame:     #times out frames to 100 ms till change 
            frame = (frame+1)%4
            nextFrame += 100 
        wall_hit = False
        quit_moving = False
        if tempx >= 480:
            wall_hit = True
            quit_moving = True
        if tempy == 135:
            wall_hit = True
            quit_moving = True
        if tempy == 500:
            wall_hit = True
            quit_moving = True
        if tempx == 75:
            wall_hit = True
            quit_moving = True
        if not wall_hit:
            showSprite(bender)
            hideSprite(dead)

        else:
            hideSprite(bender)
            showSprite(dead)

#directional events
        #all actions for if right key pressed
        if keyPressed('right'):
            if keyPressed('space'):
                #shoot right
                shooting = not shooting
                moveSprite(bubbles,bubbles.x,bubbles.y)
                bubbles.x = tempx - 50
                bubbles.y = tempy - 50
                rotateSprite(bubbles,90)
                hideSprite(reset_bubble)
                showSprite(bubbles)
            if not shooting:
                shooting = True
                bubble_direct = 'right'
            if pos_x < 2680 and tempx == 300:
                top.x -= 5
                right.x -= 5
                left.x -= 5
                bottom.x -= 5
                pos_x += 5
                moveSprite(top,top.x,top.y)
                moveSprite(right,right.x,right.y)
                moveSprite(left,left.x,left.y)
                moveSprite(bottom,bottom.x,bottom.y)
                scrollBackground(-5,0)  
                for undead in zombie_no:
                    undead.x -= 5
                changeSpriteImage(bender, 0*4+frame)
            if pos_x >= 2680 and tempx <= 480:
                tempx += 5
                changeSpriteImage(bender, 0*4+frame)
                moveSprite(bender,tempx,tempy,1)
                moveSprite(dead,tempx,tempy,1)
            elif pos_x <= -80 and tempx < 300:
                tempx += 5
                changeSpriteImage(bender, 0*4+frame)
                moveSprite(bender,tempx,tempy,1)
                moveSprite(dead,tempx,tempy,1)

        #action if going down
        elif keyPressed('down'):
            #shoot down
            if keyPressed('space'):
                shooting = not shooting
                bubbles.x = tempx - 50
                bubbles.y = tempy - 50
                moveSprite(bubbles,bubbles.x,bubbles.y)
                rotateSprite(bubbles,45)
                hideSprite(reset_bubble)
                showSprite(bubbles)
            if not shooting:
                shooting = True
                bubble_direct = 'down'
            if pos_y < 3240 and tempy == 300:
                top.y -= 5
                right.y -= 5
                left.y -= 5
                bottom.y -= 5
                pos_y += 5
                moveSprite(top,top.x,top.y)
                moveSprite(right,right.x,right.y)
                moveSprite(left,left.x,left.y)
                moveSprite(bottom,bottom.x,bottom.y)
                scrollBackground(0, -5)
                for undead in zombie_no:
                    undead.y -= 5
                changeSpriteImage(bender, 1*4+frame)
            if pos_y >= 3240 and tempy >=300 and tempy < 500:
                tempy += 5
                changeSpriteImage(bender, 1*4+frame)
                moveSprite(bender,tempx,tempy,1)
                moveSprite(dead,tempx,tempy,1)
            elif pos_y <= 0 and tempy < 300:
                tempy += 5
                changeSpriteImage(bender, 1*4+frame)
                moveSprite(bender,tempx,tempy,1)
                moveSprite(dead,tempx,tempy,1)

        #action if going left
        elif keyPressed('left'):
            #shoot up
            if keyPressed('space'):
                shooting = not shooting
                bubbles.x = tempx - 50
                bubbles.y = tempy - 50
                moveSprite(bubbles,bubbles.x,bubbles.y)
                rotateSprite(bubbles,-90)
                hideSprite(reset_bubble)
                showSprite(bubbles)
            if not shooting:
                shooting = True
                bubble_direct = 'left'
            if pos_x > -435 and tempx == 300:
                top.x += 5
                right.x += 5
                left.x += 5
                bottom.x += 5
                moveSprite(top,top.x,top.y)
                moveSprite(right,right.x,right.y)
                moveSprite(left,left.x,left.y)
                moveSprite(bottom,bottom.x,bottom.y)
                pos_x -= 5
                scrollBackground(5,0)
                for undead in zombie_no:
                    undead.x += 5
                changeSpriteImage(bender, 2*4+frame)
            if pos_x >= 2680 and tempx > 300:
                tempx -= 5
                changeSpriteImage(bender, 2*4+frame)
                moveSprite(bender,tempx,tempy,1)
                moveSprite(dead,tempx,tempy,1)
            elif pos_x == -435 and tempx >= 80:
                tempx -= 5
                changeSpriteImage(bender, 2*4+frame)
                moveSprite(bender,tempx,tempy,1)
                moveSprite(dead,tempx,tempy,1)

        #action if up is pressed
        elif keyPressed('up'):
            #shoot up
            if keyPressed('space'):
                bubbles.x = tempx - 50
                bubbles.y = tempy - 50
                shooting = not shooting
                moveSprite(reset_bubble,bubbles.x,bubbles.y)
                hideSprite(bubbles)
                showSprite(reset_bubble)
            if not shooting:
                shooting = True
                bubble_direct = 'up'
            if pos_y > 0 and tempy == 300:
                top.y += 5
                right.y += 5
                left.y += 5
                bottom.y += 5
                pos_y -= 5
                moveSprite(top,top.x,top.y)
                moveSprite(right,right.x,right.y)
                moveSprite(left,left.x,left.y)
                moveSprite(bottom,bottom.x,bottom.y)
                scrollBackground(0,5)
                for undead in zombie_no:
                    undead.y += 5
                changeSpriteImage(bender,12+frame)
            if pos_y >= 3240 and tempy >= 300:
                tempy -=5
                changeSpriteImage(bender,12+frame)
                moveSprite(bender,tempx,tempy,1)
                moveSprite(dead,tempx,tempy,1)
            elif pos_y <= 0 and tempy >= 140:
                tempy -=5
                changeSpriteImage(bender,12+frame)
                moveSprite(bender,tempx,tempy,1)
                moveSprite(dead,tempx,tempy,1)
        else:
            changeSpriteImage(bender,4)

        if bubbles.x == 250 and bubbles.y == 250:
            time.sleep(.05)
        if bubble_direct == 'right':
            bubbles.x += 5
        elif bubble_direct == 'left':
            bubbles.x -= 5
        elif bubble_direct == 'up':
            bubbles.y -= 5
        elif bubble_direct == 'down':
            bubbles.y += 5

        #zombie controls
        for undead in zombie_no:
            if undead.alive == False:
                undead.counter += 1
                if undead.counter >= 200:
                    hideSprite(undead)
            if logic_bool == 0 and undead.alive == True:
                undead.x += undead.xspeed
                if undead.x > 1000:
                    undead.x = 0
                elif undead.x < 0:
                    undead.x = 1000
                changeSpriteImage(undead,(frame%3))
                moveSprite(undead, undead.x, undead.y)
            if logic_bool == 1 and undead.alive == True:
                undead.y += undead.yspeed
                if undead.y > 750:
                    undead.y = 0
                elif undead.y < 0:
                    undead.y = 750
                changeSpriteImage(undead,frame%3+3)
                moveSprite(undead, undead.x, undead.y)
            if logic_bool == 0: logic_bool = 1
            else: logic_bool = 0
            if abs(undead.x - bubbles.x) <= 30 and abs(undead.y - bubbles.y) <= 30:
                undead.alive = False
                changeSpriteImage(undead,12)
                hideSprite(bubbles)
                hideSprite(reset_bubble)
            moveSprite(undead, undead.x, undead.y)
                
        tick(100)
        blit_no+=1
        changeSpriteImage(bubbles,frame%4)
        moveSprite(reset_bubble,bubbles.x,bubbles.y)
        moveSprite(bubbles,bubbles.x,bubbles.y)
        updateDisplay()


    endWait()

if __name__=='__main__':
    main()