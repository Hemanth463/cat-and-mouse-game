import pygame
playerSpeed = 10
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
REFRESH_RATE = 60
SCREEN_WIDTH = 1811
SCREEN_HEIGHT = 966
CLOCK = pygame.time.Clock()
pygame.font.init()
FONT = pygame.font.SysFont('opensans', 75)
FONT1 = pygame.font.SysFont('opensans', 35)
MUSIC_SCORE = './music/music.wav'
GAME_TITLE = 'Yet another Cat and Mouse Game'
MENU_IMAGE = './img/background_menu.png'
INST_IMAGE = './img/instructions.png'
PAUSE_IMG = './img/pause.png'
WIN1MSG = 'Player 1 Won!'
WIN2MSG = 'Player 2 Won!'
LOST = 'Both Lost!'
TIE = 'It is a Tie!'
COIN_IMG = './img/Coin.png'
CRYSTAL = './img/Crystal.png'
FENCE = './img/fence.png'
ROCKS = './img/Boulders.png'
BOMB = './img/Boulders.png'
MOUSE_UP = './img/Mouse_Up.png'
MOUSE_DOWN = './img/Mouse_Down.png'
CAT = './img/Cat_Right.png'
FOX = './img/Fox_Right.png'
BCKGRND = './img/background.png'
MSG1 = 'START'
MSG2 = 'END'
PLAYER1 = 'Player 1!'
PLAYER2 = 'Player 2!'
TLE = 'Oj says TLE!'
TLEFT = 'Time Left with 1: '
SCOREMSG = 'Score : '
TLEFT2 = 'Time Left with 2 : '
# SPEED of ENEMIES. SAME SPEED BELONGS TO SAME LEVEL
S1 = 7
S2 = 10
S3 = 12
