"""
The World wonderer
python world_wonderer.py title="lost pirate" bg_image=./images/background.png image=./images/zoro.png width=500 height=500 start_x=100 start_y=100
The Lost pirate of the strawhat crew that always
loses his way and has no sense of direction is
Zoro. Control him as he goes nowhere. Only place
he will find is the edge of the world.
"""
#import libraries
import pygame
import sys
import os

#Processes argv list into plain args and kwargs.
def mykwargs(argv):

    args = []
    kargs = {}
    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs

class Ocean(pygame.sprite.Sprite):
    def __init__(self, image, location):
        x = int(kwargs['width'], 10)
        y = int(kwargs['height'], 10)
        
        pygame.sprite.Sprite.__init__(self)  
        self.image = pygame.image.load(image)
        #resizes background image
        self.image = pygame.transform.scale(self.image, (x * 2, y * 2))
        self.rect = self.image.get_rect()
        #sets background image location via input
        self.rect.left, self.rect.top = location

def main(**kwargs):
    #initialize pygame
    pygame.init()
    
    #set colors
    WHITE = (255,255,255)
    RED = (255,0,0)

    #set variables and window features
    width = int(kwargs["width"],10)
    height = int(kwargs["height"],10)
    character = kwargs["image"]
    water = kwargs['bg_image']
    pygame.display.set_caption(kwargs['title'])
    start_x = int(kwargs["start_x"])
    start_y = int(kwargs["start_y"])

    #set camera inital position
    camera_x = 0
    camera_y = 0

    #set background area and filling
    space = pygame.Surface((1000,1000))
    space.fill(WHITE)
    ocean = Ocean(water, [width/5,height/5])
    
    #load character
    zoro = pygame.image.load(character)
    #character position
    x = start_x
    y = start_y

    #set screen
    screen = pygame.display.set_mode([width,height])
    
    #begin loop bool value
    running = True
    #set game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #movement for when keys get pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:   #up
            y -= 2 
            camera_y -= 2 
        if keys[pygame.K_DOWN]: #down
            y += 2 
            camera_y += 2 
        if keys[pygame.K_LEFT]: #left
            x -= 2 
            camera_x -= 2 
        if keys[pygame.K_RIGHT]:#right
            x += 2 
            camera_x += 2 

        #keeps camera in bounds
        if camera_x < (-width/10): camera_x = (-width/10)
        if camera_x > (width - (width/5)): camera_x = width - (width/5)
        if camera_y < (-height/10): camera_y = (-height/10)
        if camera_y > (height - (height/5)): camera_y = height - (height/5)

        #flags for border check
        x_min = False
        x_max = False
        y_min = False
        y_max = False
        
        #boundary check
        if x > (width): 
            x = width
            x_max = True
        if x < 0: 
            x = 0
            x_min = True
        if y > (height): 
            y = height
            y_max = True
        if y < 0: 
            y = 0
            y_min = True

        #display bacground and character
        screen.blit(space, (0, 0))
        screen.blit(ocean.image, (0 - camera_x,0 - camera_y))
        screen.blit(zoro,(x - camera_x,y - camera_y))
        
        #boarder drawing lines if character reaches edge of map
        if x_min: pygame.draw.rect(screen,RED,(width/10,(0-height/10),5,height * 5))
        if x_max: pygame.draw.rect(screen,RED,(width-5,(0-height/10),5,height * 5))
        if y_min: pygame.draw.rect(screen,RED,((0-width/10),height/10,width * 5,5))
        if y_max: pygame.draw.rect(screen,RED,((0-width/10),height-5,width*5,5))
        
        pygame.display.flip()

    #quiter
    pygame.quit()

if __name__=='__main__':
    argv = sys.argv[1:]
    #run function to allow command line input
    args,kwargs = mykwargs(argv)

    #runs main program
    main(**kwargs)