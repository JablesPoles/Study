import pygwidgets
import pygame
from pygame.locals import *

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if oWidget.handleEvent(event):
            