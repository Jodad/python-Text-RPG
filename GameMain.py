import charData
from charData import *
import colors   #R,G,B
import time
import pygame

#init method for pygame allows use of methods
pygame.init()

#*Re-Enable later*

#creates and opens window for the game to display text to
#display_width,display_height = (1200,900)
#gameDisplay = pygame.display.set_mode((display_width,display_height))
#pygame.display.set_caption('Text RPG')
#clock = pygame.time.Clock()

###############################################
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

###############################################
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
###############################################
    
def initilize():
    print("Main Menu:\n")
    option = str(input("Options:\nNew Game (N)\nLoad Save (L)\nOption (P)\n>>>"))
    if option.upper() == "N":
        print("New Game")
        newGame()
    elif option.upper() == "L":
        print("Which Save?")
        saveManager()
        
###############################################
        
def saveManager():
    print("Save open")
    #File stuff her
    #saveFile = open(Save

###############################################
def options():
    print("Nothing")
    
###############################################
def gameLoop():
    active = True
    while active:
        
        #event getter for pygame, allows player to quit using "Esc" key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #Game starts here
        move = str(input("What direction: "))

#starts the game
initilize()
