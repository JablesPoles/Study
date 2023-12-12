# Scene Demo main program with three scenes

# 1 - Import packages
import pygame
import pyghelpers

from SceneA import *
from SceneB import *
from SceneC import *

# 2 - Define constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Load assets: image(s), sound(s), etc.

# 5 - Initialize variables
# Instantiate all scenes and store them into a list
scenesList = [SceneA(window),
              SceneB(window),
              SceneC(window)]

# Create the scene manager, passing in the scenes list and the FPS
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

# Tell the scene manager to start running
oSceneMgr.run()

