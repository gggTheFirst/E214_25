import math
import stdio
import sys
import random
import pygame
import time
from pygame import mixer
##Code is as far as possible in acordance with the Python Enhancement Proposal 8 Style Guide
##Global Constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
def main():

    #Initialise pygame
    #Initialises all required pygame modules saving us trouble of doing all of them manually
    pygame.init()

    #Creates a window for the game to be displayed on
    screen = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
    welcome()
    time.sleep(5)

    #Display Space Welcome Screen


# __name__ returns "__main__" if and only if the module is called directly and not if imported
#This runs the main method when the module is run








#Methods



def welcome():
    pygame.display.set_caption("Welcome to Space Invaders")



if __name__ == "__main__":main()
