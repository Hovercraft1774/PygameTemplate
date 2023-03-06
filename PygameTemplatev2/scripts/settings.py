import os.path

import pygame as pg
import random


# define colors, colors work in a (RGB) format.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
TEAL = (0,255,255)
PINK = (255,0,255)
ORANGE = (255,127,0)
DARK_GRAY = (64,64,64)
LIGHT_GRAY = (192,192,192)
GRAY_BLUE = (92,192,194)

colors = (WHITE,BLUE,BLACK,RED,GREEN,YELLOW,TEAL,PINK,ORANGE)



#Game Title
TITLE = "CHANGE ME THIS IS WRONG!"



# Window Settings
WIDTH = 500
HEIGHT = 500
DEFAULT_COLOR = BLACK
TILE_SIZEX = WIDTH/10
TILE_SIZEY = HEIGHT/10


# camera settings
fps = 60

# file locations
#gets location of file on computer
game_folder = os.path.dirname(__file__)
game_folder = game_folder.replace("\scripts","")
sprites_folder = os.path.join(game_folder,"sprites")
playerSprites = os.path.join(sprites_folder,"playerSprites")
enemySprites = os.path.join(sprites_folder,"enemySprites")



# player Settings
solidbounds = True
bouncy = False
spawn_invincibility = True
player_img = os.path.join(playerSprites,"roboBoyStill.png")
player_img_move = os.path.join(playerSprites,"roboBoyMove.png")
player_img_down = os.path.join(playerSprites,"roboBoyDown.png")
player_img_up = os.path.join(playerSprites,"roboBoyUp.png")



# Enemy Settings

enemy_img = os.path.join(enemySprites,"enemyStill.png")
enemyCreep_img = os.path.join(enemySprites,"enemyCreepy.png")







