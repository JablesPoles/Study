# Higher or Lower - pygame ver.
# Main program

import sys
from pygame.locals import *
import pygame
import pygwidgets
from Deck import *
from Card import *
from Game import *

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 720
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30


pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

background = pygwidgets.Image(window, (0,0),
                              'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530),
                                      'New Game', width=100, height=100)
higherButton = pygwidgets.TextButton(window, (540, 520),
                                      'Higher', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520),
                                      'Lower', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530),
                                      'Quit', width=100, height=45)

oGame = Game(window)

while True:
    
    for event in pygame.event.get():
        if((event.type == QUIT) or ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
        (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()
        
        if newGameButton.handleEvent(event):
            oGame.reset()
            lowerButton.enable()
            higherButton.enable()
                
        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
                
        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()
                
    background.draw()
    
    oGame.draw()
    
    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()
    
    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)