import sys
import os
import pprint
import pygame
import math

from helper_module import mykwargs
#pull key logging commands from library
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#class for the background image
class Ocean(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) 
        
        #locates image for background
        self.image = pygame.image.load(os.path.join('images', "ocean.png"))
        self.rect = self.image.get_rect()
        
        #places image
        self.rect.left, self.rect.top = location

class Player(pygame.sprite.Sprite):
    #initalize calss
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #locates image for character sprite
        self.image = pygame.image.load(os.path.join('images', "zoro.png"))
        
        #resizes sprite based on command line input
        self.image = pygame.transform.scale(self.image, (int(kwargs['pwidth']), int(kwargs['pheight'])))
        self.rect = self.image.get_rect()
        
        #places sprite in center of window
        self.rect.center = (int(int(kwargs['width']) / 2), int(int(kwargs['height']) /2))
        self.speed = 5
    #event capturing to force movement
    def update(self,keys):
        if keys[K_UP]
            self.y -= self.speed
        elif keys[K_DOWN]
            self.y += self.speed
        elif keys[K_LEFT]
            self.x -= self.speed
        elif keys[K_RIGHT]
            self.x += self.speed

def main(**kwargs):
    pygame.init()
    pygame.mixer.init()

    #screen height from command line
    width = int(kwargs['width'])
    height = int(kwargs['height'])

    #load parameters nd title
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(kwargs['title'])

    #initialize character and load background
    Sprites = pygame.sprite.Group()
    player = Player()
    Sprites.add(player)
    ocean = Ocean('ocean.png', [0,0])

    running = True
    while running:
        #when to close
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        
        #draw images to screen
        screen.fill([255,255,255])
        screen.blit(ocean.image, ocean.rect)
        Sprites.draw(screen)
        
        #update postion with events
        pressed_keys = pygame.key.get_pressed()
        Sprites.update(pressed_keys)
        pygame.display.flip()
    quit()

def usage():
    # Params in square brackets are optional
    # The kwargs function script needs key=value to NOT have spaces
    print("Usage: python LostPirate.py title=string img_path=string width=int height=int [jsonfile=string]")
    print("Example:\n\n\t python LostPirate.py title='Wonderer' img_path=./images/zoro.png width=500 height=500 pwidth=100 pheight=100\n")
    sys.exit()

if __name__=='__main__':
    """
    This example has 4 required parameters, so after stripping the file name out of
    the list argv, I can test the len() of argv to see if it has 4 params in it.
    """
    argv = sys.argv[1:]

    if len(argv) < 6:
        print(len(argv))
        usage()

    args,kwargs = mykwargs(argv)

    # here you have a dictionary with all your parameters in it
    print("Printing dictionary from name == main:")
    pprint.pprint(kwargs)

    # you could send all of them to a main function
    main(**kwargs)