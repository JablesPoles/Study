from pygame.locals import *
import pygame
import sys
import pygwidgets
from BalloonMgr import *

# 2 - Define constants

BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets
oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25),
                                       'Score: 0', textColor=BLACK,
                                       backgroundColor=None, width=140, fontSize=24)
oStatusDisplay = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25),
                                        '', textColor=BLACK, backgroundColor=None)
oStartButton = pygwidgets.DisplayText(window, (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10),
                                      'Start')

# 5 - Initialize variables
oBalloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False # wait until user clicks Start

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    nPointsEarned = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if playing:
            oBalloonMgr.handleEvent(event)
            theScore = oBalloonMgr.getScore()
            oScoreDisplay.setValue('Score: ' + str(theScore))
        elif oStartButton.handleEvent(event):
            oBalloonMgr.start()
            oScoreDisplay.setValue('Score: 0')
            playing = True
            oStartButton.disable()
            
    # 8 - Do any 'per frame' actions
    if playing:
        oBalloonMgr.update()
        nPopped = oBalloonMgr.getCountPopped()
        nMissed = oBalloonMgr.getCountMissed()
        oStatusDisplay.setValue('Popped: ' + str(nPopped) +
                                '   Missed: ' + str(nMissed) +
                                '   Out of: ' + str(N_BALLOONS))
        
        if (nPopped + nMissed) == N_BALLOONS:
            playing = False
            oStartButton.enable()
            
    window.fill(BACKGROUND_COLOR)
    
    if playing:
        oBalloonMgr.draw()
        
    pygame.draw.rect(window, GRAY, pygame.Rect(0,
                    USABLE_WINDOW_HEIGHT, WINDOW_WIDTH, PANEL_HEIGHT))
    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oStartButton.draw()
    
    pygame.display.update()
    
    clock.tick(FRAMES_PER_SECOND)