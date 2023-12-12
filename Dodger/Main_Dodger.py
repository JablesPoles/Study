import pygame
import pyghelpers
import pygwidgets
from Constants import *
from pygame.locals import *

# Instantiate all scenes and store them in a list
scenesList = [SceneSplash(window),
              SceneHighScores(window),
              ScenePlay(window)]

# Create the scene manager, passing in the scenes list and the FPS
oSceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

# Tell the scene manager to start running
oSceneMgr.run()