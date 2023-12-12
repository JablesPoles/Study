# Scene A

import pygwidgets
import pyghelpers
import pygame
from pygame.locals import *
from Constants import *

class SceneA(pyghelpers.Scene):
    def __init__(self, window):
        
        self.window = window
        
        self.messageField = pygwidgets.DisplayText(self.window,
                    (15, 25), 'This is Scene A', fontSize=50,
                    textColor=WHITE, width=610, justified='center')
        
        self.goToAButton = pygwidgets.TextButton(self.window,
                    (250, 100), 'Go to Scene A')
        
        self.goToBButton = pygwidgets.TextButton(self.window,
                    (250, 100), 'Go to Scene B')
        
        self.goToCButton = pygwidgets.TextButton(self.window,
                    (400, 100), 'Go to Scene C')
        
        self.goToAButton.disable()
        
    def getSceneKey(self):
        return SCENE_A
    
    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.goToBButton.handleEvent(event):
                self.goToScene(SCENE_B)
            if self.goToCButton.handleEvent(event):
                self.goToScene(SCENE_C)
                
    def draw(self):
        self.window.fill(GRAYA)
        self.messageField.draw()
        self.goToAButton.draw()
        self.goToBButton.draw()
        self.goToCButton.draw()
        