# File Name: ToonyWars.py
# Description: Game
# Author: Jonathan Yam, Leo
# Date: 11/29/2018


# -----------------------------------------------------------------------------------------------------------------------
# initialise pygame
# create variables
# load pictures

import pygame
import math
import random

pi = math.pi
pygame.init()
WIDTH = 1200
HEIGHT = 700
TOP = 0
BOTTOM = 480
gameWindow = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 64)
GREEN = (0, 128, 0)
BLUE = (0, 255, 255)
WHITE = (255, 255, 255)
GREY = (72, 72, 72)
BROWN = (185, 122, 87)
outline = 0
gameDirectory = "images"
clock = pygame.time.Clock()
windowRealitiveX = 0
mapRealitiveX = 0
frame = 0
realFrame = 0

#variable to keep track of volume
musicVolume = 0.5
soundVolume = 0.3

# note: fps needs to be set to a multiple of 10, otherwise, it will cause error is animation rate or troop speed
fps = 60
gameWindowMoveSpeed = 900 / fps

#Sword Sound effect
slashSword = pygame.mixer.Sound('slashSword.wav')
slashSword.set_volume(soundVolume)
bazookaSound = pygame.mixer.Sound('bazooka.wav')
bazookaSound.set_volume(soundVolume)
fireDragonSound = pygame.mixer.Sound('flamestrike.wav')
fireDragonSound.set_volume(soundVolume)
hellSnakeSound = pygame.mixer.Sound('hellSnake.wav')
hellSnakeSound.set_volume(soundVolume)


background = pygame.image.load("background.png").convert_alpha()
mainMenuScreen = pygame.image.load("main menu.png").convert_alpha()
settingScreen = pygame.image.load("setting.png").convert_alpha()
levelScreen = pygame.image.load("level selection.png").convert_alpha()
player1UI = pygame.image.load("player1UI.png").convert_alpha()
player2UI = pygame.image.load("player2UI.png").convert_alpha()
singlePlayerUI = pygame.image.load("singlePlayerUI.png").convert_alpha()
font1 = pygame.font.SysFont("ALGERIAN", 10)
font2 = pygame.font.SysFont("ALGERIAN", 25)
font3 = pygame.font.SysFont("ALGERIAN", 50)
backgroundXY = background.get_rect()
button1 = pygame.image.load("button1.png").convert_alpha()
instrunctionPic = pygame.image.load("instructions text.png").convert_alpha()

# add pictures of game over screens
player1WinPic = pygame.image.load("player 1 win.png").convert_alpha()
player2WinPic = pygame.image.load("player 2 win.png").convert_alpha()
singleWinPic = pygame.image.load("you win.png").convert_alpha()
singleLosePic = pygame.image.load("you lose.png").convert_alpha()

# player 1 lists for the values and states of troops
player1TroopNumList = []
player1TroopTypeList = []
player1TroopStateList = []
player1TroopXList = []
player1TroopYList = []
player1TroopHealthList = []

# player 2 lists for the values and states of troops
player2TroopNumList = []
player2TroopTypeList = []
player2TroopStateList = []
player2TroopXList = []
player2TroopYList = []
player2TroopHealthList = []

# lists to keep track of the animations player 1
swordManPic = []
bombManPic = []
fireDragonPic = []
hellSnakePic = []

# lists to keep track of the animations player 2
player2SwordManPic = []
player2BombManPic = []
player2FireDragonPic = []
player2HellSnakePic = []

# variables to keep track of single player level
level = False

# variable to keep track of when to spawn next computer troop
nextSpawn = 0
nextSpawnFrame = 0
computerSpawn = False

# variables to change diffuculty (computer spawn rate and computer spawn troop type)
# type of troop to spawn eg. 1 = swordman, 2 = bombman
level1ComputerSpawn = random.randint(0, 2)
level2ComputerSpawn = random.randint(0, 3)
level3ComputerSpawn = random.randint(0, 4)

# time delay between each spawn (frames)
level1ComputerSpawnDelay = random.randint(60, 90)
level2ComputerSpawnDelay = random.randint(30, 60)
level3ComputerSpawnDelay = random.randint(10, 30)

# variable to set level confriguations once in single player
setLevel = True

# Tower Properties
tower = "tower"
player1TowerPic = pygame.image.load("tower1.png").convert_alpha()
player2TowerPic = pygame.image.load("tower2.png").convert_alpha()
player1TowerX = backgroundXY[0] + 20 + mapRealitiveX
player1TowerY = BOTTOM - 320
player2TowerX = backgroundXY[2] - 200 + mapRealitiveX
player2TowerY = BOTTOM - 320
player1TowerHP = 100000
player2TowerHP = 100000

# player 1 troop properties
# Sword Man Properties
swordMan = "swordMan"
numOfSwordManPics = 6
for i in range(numOfSwordManPics):
    swordManPic.append(pygame.image.load("swordman" + str(i) + ".png").convert_alpha())
swordManPicNum = 0
swordManX = 100 + mapRealitiveX
swordManY = 330
swordManSpeedX = 60.0 / fps
swordManHP = 2000
swordManW = 130
swordManH = 130
player1SwordmanRange = -50
player1SwordmanDamage = 1800 / fps
player1SwordmanCost = 3

# bomb man properties
bombMan = "bombMan"
numOfBombManPics = 6
for i in range(numOfBombManPics):
    bombManPic.append(pygame.image.load("bombman" + str(i) + ".png").convert_alpha())
bombManPicNum = 0
bombManX = 100 + mapRealitiveX
bombManY = 330
bombManSpeedX = 60.0 / fps
bombManHP = 500
bombManW = 130
bombManH = 130
player1BombManRange = -300
player1BombManDamage = 6000 / fps
player1BombManCost = 10

# dragon Properties
dragon = "dragon"
numOfFireDragonPics = 6
for i in range(numOfFireDragonPics):
    fireDragonPic.append(pygame.image.load("dragon" + str(i) + ".png").convert_alpha())
fireDragonPicNum = 0
fireDragonX = 100 + mapRealitiveX
fireDragonY = 150
fireDragonSpeedX = 120.0 / fps
fireDragonHP = 5000
fireDragonW = 130
fireDragonH = 130
player1DragonRange = -200
player1DragonDamage = 3000 / fps
player1DragonCost = 15

# snake Properties
snake = "snake"
numOfHellSnakePics = 6
for i in range(numOfHellSnakePics):
    hellSnakePic.append(pygame.image.load("hellsnake" + str(i) + ".png").convert_alpha())
hellSnakePicNum = 0
hellSnakeX = 100 + mapRealitiveX
hellSnakeY = 320
hellSnakeSpeedX = 60.0 / fps
hellSnakeHP = 20000
hellSnakeW = 260
hellSnakeH = 140
player1HellSnakeRange = -200
player1HellSnakeDamage = 600 / fps
player1HellSnakeCost = 20

# player 2 troop properties
# swordman properties
swordMan = "swordMan"
numOfSwordManPics = 6
for i in range(numOfSwordManPics):
    player2SwordManPic.append(pygame.image.load("player2swordman" + str(i) + ".png").convert_alpha())
swordManPicNum = 0
player2SwordManX = backgroundXY[2] - 220 + mapRealitiveX
swordManY = 330
swordManSpeedX = 60.0 / fps
swordManHP = 2000
swordManW = 130
swordManH = 130
player2SwordmanRange = 50
player2SwordmanDamage = 1800 / fps
player2SwordmanCost = 3

# bomb man properties
bombMan = "bombMan"
numOfBombManPics = 6
for i in range(numOfBombManPics):
    player2BombManPic.append(pygame.image.load("player2bombman" + str(i) + ".png").convert_alpha())
bombManPicNum = 0
player2BombManX = backgroundXY[2] - 220 + mapRealitiveX
bombManY = 330
bombManSpeedX = 60.0 / fps
bombManHP = 500
bombManW = 130
bombManH = 130
player2BombManRange = 300
player2BombManDamage = 6000 / fps
player2BombManCost = 10

# dragon Properties
dragon = "dragon"
numOfFireDragonPics = 6
for i in range(numOfFireDragonPics):
    player2FireDragonPic.append(pygame.image.load("player2dragon" + str(i) + ".png").convert_alpha())
fireDragonPicNum = 0
player2FireDragonX = backgroundXY[2] - 220 + mapRealitiveX
fireDragonY = 150
fireDragonSpeedX = 120.0 / fps
fireDragonHP = 5000
fireDragonW = 130
fireDragonH = 130
player2DragonRange = 200
player2DragonDamage = 3000 / fps
player2DragonCost = 15

# snake Properties
snake = "snake"
numOfHellSnakePics = 6
for i in range(numOfHellSnakePics):
    player2HellSnakePic.append(pygame.image.load("player2snake" + str(i) + ".png").convert_alpha())
hellSnakePicNum = 0
player2HellSnakeX = backgroundXY[2] - 220 + mapRealitiveX
hellSnakeY = 320
hellSnakeSpeedX = 60.0 / fps
hellSnakeHP = 20000
hellSnakeW = 260
hellSnakeH = 140
player2HellSnakeRange = 200
player2HellSnakeDamage = 600 / fps
player2HellSnakeCost = 20

backgroundX = 0
backgroundY = 0
letterX = 320
letterY = 240

player1Tower = True
player2Tower = True

# mana
player1Mana = 0
player2Mana = 0

player1ManaIncrease = 6.0
player2ManaIncrease = 6.0

player1StartingMana = 100
player2StartingMana = 100

# variable to enable StartingMana function
giveStartingMana = True

# flag to close program when hit escape key
inPlay = True
gameOver = False

# variables to keep track of which screen you're on
menu = False
setting = False
singlePlayer = False
multiplayer = False
levelSelection = False
instructions = False

# variable to keep track of which player won
player1Win = False
player2Win = False

singleWin = False
singleLose = False

# variables for first troops for each player
player1FirstTroop = False
player2FirstTroop = False

player1FirstTroopIndex = False
player2FirstTroopIndex = False

# mouse clicking
mouseClick = False
previousClick = False


# -----------------------------------------------------------------------------------------------------------------------
# all function used


# funciton to detect when mouse is clicked down
# using this function , resetMouseDown, and mousePosition() so that 1 click = deploy 1 troop
# otherwise, troops will deploy as long as mouse is pressed
def mouseDown():
    global mouseClick
    global previousClick

    if event.type == pygame.MOUSEBUTTONUP:
        mouseClick = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouseClick = True
        previousClick = mouseClick


# reset click
def resetMouseDown():
    global mouseClick
    global previousClick
    previousClick = False


# function for mouse clicking buttons in game
def mousePosition(x1, x2, y1, y2):
    global previousClick
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN and previousClick:

        if x1 < mouseX < x2 and y1 < mouseY < y2:
            return True

        else:
            return False


# move screen left or right when hovering on sides of game
def moveScreen(x1, x2, y1, y2):
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if x1 < mouseX < x2 and y1 < mouseY < y2:
        return True

    else:
        return False


# see if mouse is hovering over a certain position
def mouseHover(x1, x2, y1, y2):
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if x1 < mouseX < x2 and y1 < mouseY < y2:
        return True

    else:
        return False


''' or (
            # clicking back button on main menu
            menu == True and event.type == pygame.MOUSEBUTTONDOWN and 410 < mouseX < 520 and 540 < mouseY < 650):'''

# function to close everything when escape key is pressed
def exitKey():
    global inPlay
    global menu
    global setting
    global levelSelection
    global multiplayer
    global singlePlayer
    global player1Win
    global player2Win
    global singleWin
    global singleLose
    global instructions

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    # escape key
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or (
            # clicking back button on main menu
            menu == True and event.type == pygame.MOUSEBUTTONDOWN and 410 < mouseX < 520 and 540 < mouseY < 650):

        inPlay = False
        menu = False
        setting = False
        levelSelection = False
        multiplayer = False
        singlePlayer = False
        player1Win = False
        player2Win = False
        singleWin = False
        singleLose = False
        instructions = False



# function for mouse click to start single player/ multiplayer / setting
#also loads music, and set music volume
# opens level selection when clicked
def mouseMainMenuSingle(x1, x2, y1, y2):
    global menu
    global levelSelection
    global slashSword
    global bazookaSound
    global fireDragonSound
    global hellSnakeSound

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:

            menu = False
            levelSelection = True

            pygame.mixer.music.load('backgroundMusic.mp3')
            pygame.mixer.music.set_volume(musicVolume)
            pygame.mixer.music.play(-1)

            slashSword.set_volume(soundVolume)
            bazookaSound.set_volume(soundVolume)
            fireDragonSound.set_volume(soundVolume)
            hellSnakeSound.set_volume(soundVolume)


# opens multiplayer when clicked
def mouseMainMenuMulti(x1, x2, y1, y2):
    global menu
    global multiplayer
    global slashSword
    global bazookaSound
    global fireDragonSound
    global hellSnakeSound

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:

            menu = False
            multiplayer = True

            pygame.mixer.music.load('backgroundMusic.mp3')
            pygame.mixer.music.set_volume(musicVolume)
            pygame.mixer.music.play(-1)
            slashSword.set_volume(soundVolume)
            bazookaSound.set_volume(soundVolume)
            fireDragonSound.set_volume(soundVolume)
            hellSnakeSound.set_volume(soundVolume)


# open or close setting
def mouseSetting(x1, x2, y1, y2, close, open):
    global menu
    global setting

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:
            menu = close
            setting = open


# opens or closes instructions
def mouseInstructions(x1, x2, y1, y2, close, open):
    global menu
    global instructions

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:
            menu = close
            instructions = open


# back button when on level selection
def mouseBackLevelSelection(x1, x2, y1, y2, open, close):
    global menu
    global levelSelection

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:
            menu = open
            levelSelection = close


# back button in single player botton right corner
def mouseBackSinglePlayer(x1, x2, y1, y2):
    global menu, singlePlayer

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:
            menu = True
            singlePlayer = False

            # reset all variables after exiting
            resetAll()


# runction for changing frames per second settings
def mouseSettingFPS(x1, x2, y1, y2, frame):
    global fps

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:
            fps = frame

#function to change music volume in setting
def mouseSettingBackgroundMusic(x1, x2, y1, y2, volume):
    global musicVolume

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:
            musicVolume = volume

#function to change sound volume in setting
def mouseSettingSoundEffect(x1, x2, y1, y2, volume):
    global soundVolume

    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:
            soundVolume = volume


# function to redraw button in setting after they are clicked on
def redrawButton(x, y):
    gameWindow.blit(button1, (x, y))


# if mouse is hovering over troop deployment buttons, show troop stats in description box
def troopDescription(health, damage, range, speed, cost, x, y):
    # descriptions of troop

    troopHealth = font2.render("Health: " + str(health), 1, BLACK)
    gameWindow.blit(troopHealth, (x, y))

    troopDamage = font2.render("Damage: " + str(damage), 1, BLACK)
    gameWindow.blit(troopDamage, (x, y + 25))

    troopRange = font2.render("Range: " + str(range), 1, BLACK)
    gameWindow.blit(troopRange, (x, y + 50))

    troopSpeed = font2.render("Speed: " + str(speed), 1, BLACK)
    gameWindow.blit(troopSpeed, (x, y + 75))

    troopCost = font2.render("Cost: " + str(cost), 1, BLACK)
    gameWindow.blit(troopCost, (x, y + 100))


# function for grid
def grid():
    for x in range(0, WIDTH, 10):
        pygame.draw.line(gameWindow, BLUE, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, 10):
        pygame.draw.line(gameWindow, BLUE, (0, y), (WIDTH, y), 1)
    for x in range(0, WIDTH, 10 * 10):
        pygame.draw.line(gameWindow, GREY, (x, 0), (x, HEIGHT), 2)
    for y in range(0, HEIGHT, 10 * 10):
        pygame.draw.line(gameWindow, GREY, (0, y), (WIDTH, y), 2)


# functions to redraw different screens / maps
# function for main menu
def mainMenu():
    gameWindow.fill(WHITE)
    gameWindow.blit(mainMenuScreen, (0, 0))


# function for multiplayer map
def redrawGameWindow():
    gameWindow.fill(WHITE)
    gameWindow.blit(background, (mapRealitiveX, 0))


def redrawSetting():
    gameWindow.fill(WHITE)
    gameWindow.blit(mainMenuScreen, (0, 0))
    gameWindow.blit(settingScreen, (305, 70))


def redrawlevelSelection():
    gameWindow.fill(WHITE)
    gameWindow.blit(mainMenuScreen, (0, 0))
    gameWindow.blit(levelScreen, (305, 70))


def redrawInstructions():
    gameWindow.fill(WHITE)
    gameWindow.blit(mainMenuScreen, (0, 0))
    gameWindow.blit(instrunctionPic, (172, 10))


# function for game over screen
def redrawPlayer1Win():
    gameWindow.blit(player1WinPic, (305, 70))


def redrawPlayer2Win():
    gameWindow.blit(player2WinPic, (305, 70))


def redrawSingleWin():
    gameWindow.blit(singleWinPic, (305, 70))


def redrawSingleLose():
    gameWindow.blit(singleLosePic, (305, 70))


# function to draw UI elements
# draw UI box
def drawPlayer1UI():
    gameWindow.blit(player1UI, (0, 500))


def drawPlayer2UI():
    gameWindow.blit(player2UI, (600, 500))


def drawsinglePlayerUI():
    gameWindow.blit(singlePlayerUI, (0, 500))


# writes level in single player UI
# only doing this because don't know what to put there
def drawLevel():
    levelNum = font3.render("Level  " + str(level), 1, BLACK)
    gameWindow.blit(levelNum, (700, 575))


# function to draw mana
def drawPlayer1Mana(mana, x):
    manaHeight = mana * 1.4
    manaY = 140 - manaHeight
    pygame.draw.rect(gameWindow, BLUE, (x, 530 + manaY, 70, manaHeight), 0)


# constantly add mana to player
def player1AddMana():
    global player1Mana
    if player1Mana < 100:
        player1Mana += player1ManaIncrease / fps


def player2AddMana():
    global player2Mana
    if player2Mana < 100:
        player2Mana += player1ManaIncrease / fps


# function to draw player 1 tower
def drawAllyTower():
    if any("tower" in s for s in player1TroopTypeList):

        if player1TroopHealthList[player1TroopTypeList.index("tower")] > 0:
            gameWindow.blit(player1TowerPic, (player1TowerX + mapRealitiveX, player1TowerY))
            letterGraphics = font2.render("HP: " + str(player1TroopHealthList[player1TroopTypeList.index("tower")]), 1,
                                          BLACK)
            gameWindow.blit(letterGraphics, (player1TowerX + mapRealitiveX, player1TowerY))


# function to draw layer 2 tower
def drawEnemyTower():
    if any("tower" in s for s in player2TroopTypeList):

        if player2TroopHealthList[player2TroopTypeList.index("tower")] > 0:
            gameWindow.blit(player2TowerPic, (player2TowerX + mapRealitiveX, player2TowerY))
            letterGraphics = font2.render("HP: " + str(player2TroopHealthList[player2TroopTypeList.index("tower")]), 1,
                                          BLACK)
            gameWindow.blit(letterGraphics, (player2TowerX + mapRealitiveX, player2TowerY))


# function for deploying different types of troops for player 1
def player1DeployTroop(keys, troopType, troopState, troopX, troopY, troopHealth, troopCost):
    global player1Mana

    if keys is True and player1Mana >= troopCost:
        player1Mana -= troopCost
        player1TroopTypeList.append(troopType)
        player1TroopStateList.append(troopState)
        player1TroopXList.append(troopX)
        player1TroopYList.append(troopY)
        player1TroopHealthList.append(troopHealth)


# function for deploying different types of troops for player 2
def player2DeployTroop(keys, troopType, troopState, troopX, troopY, troopHealth, troopCost):
    global player2Mana

    if keys is True and player2Mana >= troopCost:
        player2Mana -= troopCost
        player2TroopTypeList.append(troopType)
        player2TroopStateList.append(troopState)
        player2TroopXList.append(troopX)
        player2TroopYList.append(troopY)
        player2TroopHealthList.append(troopHealth)


# function for deploying different types of troops for computer
def computerDeployTroop(keys, troopType, troopState, troopX, troopY, troopHealth):
    if keys is True:
        player2TroopTypeList.append(troopType)
        player2TroopStateList.append(troopState)
        player2TroopXList.append(troopX)
        player2TroopYList.append(troopY)
        player2TroopHealthList.append(troopHealth)


# function for sound effects
def player1SoundEffect(troopType):
    if player1TroopTypeList[player1NumTroop] == "swordMan" and player1TroopStateList[player1NumTroop] == "attacking":
        slashSword.play()
    elif player1TroopTypeList[player1NumTroop] == "bombMan" and player1TroopStateList[player1NumTroop] == "attacking":
        bazookaSound.play()
    elif player1TroopTypeList[player1NumTroop] == "dragon" and player1TroopStateList[player1NumTroop] == "attacking":
        fireDragonSound.play()
    elif player1TroopTypeList[player1NumTroop] == "snake" and player1TroopStateList[player1NumTroop] == "attacking":
        hellSnakeSound.play()


def player2SoundEffect(troopType):
    if player2TroopTypeList[player2NumTroop] == "swordMan" and player2TroopStateList[player2NumTroop] == "attacking":
        slashSword.play()
    elif player2TroopTypeList[player2NumTroop] == "bombMan" and player2TroopStateList[player2NumTroop] == "attacking":
        bazookaSound.play()
    elif player2TroopTypeList[player2NumTroop] == "dragon" and player2TroopStateList[player2NumTroop] == "attacking":
        fireDragonSound.play()
    elif player2TroopTypeList[player2NumTroop] == "snake" and player2TroopStateList[player2NumTroop] == "attacking":
        hellSnakeSound.play()


# function for annimating and changing the state of troops
def player1AnnimateAndMoveTroops(troopType, troopRange, troopSpeed, troopPic, troopY):
    # if troop is certain type and has health
    if player1TroopTypeList[player1NumTroop] == troopType and player1TroopHealthList[player1NumTroop] > 0:

        # changes state to moving when there are no enemies in front
        player1TroopStateList[player1NumTroop] = "moving"

        # if there are enemy troops other than enemy tower
        if len(player2TroopTypeList) > 1:

            # change state to attacking when enemy in front
            if player1TroopXList[player1NumTroop] >= player2FirstTroop + troopRange:
                player1TroopStateList[player1NumTroop] = "attacking"

        # if there is only enemy tower
        elif len(player2TroopTypeList) == 1:

            # changes state to attacking when tower in front
            if player1TroopXList[player1NumTroop] >= player2FirstTroop + troopRange:
                player1TroopStateList[player1NumTroop] = "attacking"

        if player1TroopStateList[player1NumTroop] == "moving":
            # moving annimation
            player1TroopXList[player1NumTroop] += troopSpeed
            gameWindow.blit(troopPic[frame % 3 + 3],
                            (player1TroopXList[player1NumTroop] + mapRealitiveX, player1TroopYList[player1NumTroop]))
            letterGraphics = font1.render("HP: " + str(player1TroopHealthList[player1NumTroop]), 1, BLACK)
            gameWindow.blit(letterGraphics, (player1TroopXList[player1NumTroop] + mapRealitiveX + 30, troopY))

        elif player1TroopStateList[player1NumTroop] == "attacking" and len(player2TroopHealthList) > 0:
            # attacking animation
            player2TroopHealthList[player2FirstTroopIndex] -= player1SwordmanDamage
            gameWindow.blit(troopPic[frame % 3],
                            (player1TroopXList[player1NumTroop] + mapRealitiveX, player1TroopYList[player1NumTroop]))
            letterGraphics = font1.render("HP: " + str(player1TroopHealthList[player1NumTroop]), 1, BLACK)
            gameWindow.blit(letterGraphics, (player1TroopXList[player1NumTroop] + mapRealitiveX + 30, troopY))


def player2AnnimateAndMoveTroops(troopType, troopRange, troopSpeed, troopPic, troopY):
    if player2TroopTypeList[player2NumTroop] == troopType and player2TroopHealthList[player2NumTroop] > 0:

        # changes state to moving when there are no enemies in front
        player2TroopStateList[player2NumTroop] = "moving"

        # if there are enemy troops other than enemy tower
        if len(player1TroopTypeList) > 1:

            # change state to attacking when enemy in front
            if player2TroopXList[player2NumTroop] <= player1FirstTroop + troopRange:
                player2TroopStateList[player2NumTroop] = "attacking"

        # if there is only enemy tower
        elif len(player1TroopTypeList) == 1:

            # changes state to attacking when tower in front
            if player2TroopXList[player2NumTroop] <= player1FirstTroop + troopRange:
                player2TroopStateList[player2NumTroop] = "attacking"

        if player2TroopStateList[player2NumTroop] == "moving":
            # moving annimation
            player2TroopXList[player2NumTroop] -= troopSpeed
            gameWindow.blit(troopPic[frame % 3 + 3],
                            (player2TroopXList[player2NumTroop] + mapRealitiveX, player2TroopYList[player2NumTroop]))
            letterGraphics = font1.render("HP: " + str(player2TroopHealthList[player2NumTroop]), 1, BLACK)
            gameWindow.blit(letterGraphics, (player2TroopXList[player2NumTroop] + mapRealitiveX + 30, troopY))

        elif player2TroopStateList[player2NumTroop] == "attacking" and len(player1TroopHealthList) > 0:
            # attacking animation
            player1TroopHealthList[player1FirstTroopIndex] -= player2SwordmanDamage
            gameWindow.blit(troopPic[frame % 3],
                            (player2TroopXList[player2NumTroop] + mapRealitiveX, player2TroopYList[player2NumTroop]))
            letterGraphics = font1.render("HP: " + str(player2TroopHealthList[player2NumTroop]), 1, BLACK)
            gameWindow.blit(letterGraphics, (player2TroopXList[player2NumTroop] + mapRealitiveX + 30, troopY))


# function to end game and display a game over screen

# variables that keep track of which keys are presssed
# reset deployment keys at the start of each frame/loop
def resetKeys():
    global key1
    global key2
    global key3
    global key4
    global key7
    global key8
    global key9
    global key0

    key1 = False
    key2 = False
    key3 = False
    key4 = False
    key7 = False
    key8 = False
    key9 = False
    key0 = False


# everything on map is realitive to reference point mapRealitiveX
# move mapRealitiveX when pressing K_right or K_left or moveScreen() with mouse input
def moveGameWindow():
    global mapRealitiveX

    keys = pygame.key.get_pressed()

    # moves the map
    if keys[pygame.K_RIGHT] and mapRealitiveX > - backgroundXY[2] + WIDTH:
        mapRealitiveX -= gameWindowMoveSpeed

    elif moveScreen(1100, 1200, 0, 500) and mapRealitiveX > - backgroundXY[2] + WIDTH:
        mapRealitiveX -= gameWindowMoveSpeed

    if keys[pygame.K_LEFT] and mapRealitiveX < 0:
        mapRealitiveX += gameWindowMoveSpeed

    elif moveScreen(0, 100, 0, 500) is True and mapRealitiveX < 0:

        mapRealitiveX += gameWindowMoveSpeed


# make key# variables true when keyboard or mouse is pressed
def keysPressed():
    global key1
    global key2
    global key3
    global key4
    global key7
    global key8
    global key9
    global key0

    keys = pygame.key.get_pressed()

    # player 1 press keys 1,2,3 to summon troop
    if keys[pygame.K_1] or mousePosition(30, 110, 530, 590) is True:
        key1 = True

    if keys[pygame.K_2] or mousePosition(135, 215, 530, 590) is True:
        key2 = True

    if keys[pygame.K_3] or mousePosition(30, 110, 610, 670) is True:
        key3 = True

    if keys[pygame.K_4] or mousePosition(135, 215, 610, 670) is True:
        key4 = True

    # player 2 press keys 7,8,9 to summon troop
    if keys[pygame.K_7] or mousePosition(630, 710, 530, 590) is True:
        key7 = True

    if keys[pygame.K_8] or mousePosition(735, 815, 530, 590) is True:
        key8 = True

    if keys[pygame.K_9] or mousePosition(630, 710, 610, 670) is True:
        key9 = True

    if keys[pygame.K_0] or mousePosition(735, 815, 610, 670) is True:
        key0 = True


# finds the closest troop, and mark them as the troop to be targeted by other team
def player1Targeted():
    global player1FirstTroop
    global player1FirstTroopIndex

    # mark closest player 1 troop to be targeted
    if len(player1TroopTypeList) > 0:
        player1FirstTroop = max(player1TroopXList)
        player1FirstTroopIndex = player1TroopXList.index(max(player1TroopXList))


def player2Targeted():
    global player2FirstTroop
    global player2FirstTroopIndex

    # mark closest player 2 troop to be targeted
    if len(player2TroopTypeList) > 0:
        player2FirstTroop = min(player2TroopXList)
        player2FirstTroopIndex = player2TroopXList.index(min(player2TroopXList))


# remove troops variables from lists after they die
def removeTroops(Index, HealthList, TypeList, StateList, XList, YList):
    try:
        if HealthList[Index] < 0:
            del TypeList[Index]
            del StateList[Index]
            del XList[Index]
            del YList[Index]
            del HealthList[Index]
    except:
        pass


# setting starting mana
def startingMana(player1, player2):
    global giveStartingMana

    global player1Mana
    global player2Mana
    if giveStartingMana is True:
        player1Mana = player1
        player2Mana = player2
        giveStartingMana = False


# after fps is changed in the settings, variables need to be changed in order to keep the same ratio
# function to change troops speed and damage ratio after fps change
def changeTroopSpeedFps():
    global swordManSpeedX
    global bombManSpeedX
    global fireDragonSpeedX
    global hellSnakeSpeedX
    global player1SwordmanDamage
    global player2SwordmanDamage
    global player1BombManDamage
    global player2BombManDamage
    global player1DragonDamage
    global player2DragonDamage
    global player1HellSnakeDamage
    global player2HellSnakeDamage

    swordManSpeedX = 60.0 / fps
    bombManSpeedX = 60.0 / fps
    fireDragonSpeedX = 120.0 / fps
    hellSnakeSpeedX = 60.0 / fps
    player1SwordmanDamage = 1800 / fps
    player2SwordmanDamage = 1800 / fps
    player1BombManDamage = 6000 / fps
    player2BombManDamage = 6000 / fps
    player1DragonDamage = 3000 / fps
    player2DragonDamage = 3000 / fps
    player1HellSnakeDamage = 600 / fps
    player2HellSnakeDamage = 600 / fps


def changeWindowMoveSpeedFps():
    global gameWindowMoveSpeed

    gameWindowMoveSpeed = 900.0 / fps


# select level in level selection screen
def mouseLevelSelection(x1, x2, y1, y2):
    global previousClick
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN and previousClick:

        if x1 < mouseX < x2 and y1 < mouseY < y2:
            return True

        else:
            return False


# function to keep track of the difficulty
def selectDifficulty(x1, x2, y1, y2, levelSelect):
    global level
    global singlePlayer
    global levelSelection

    if mousePosition(x1, x2, y1, y2) is True:
        level = levelSelect
        singlePlayer = True
        levelSelection = False


# function for computer to spawn troops
# spawn delay and spawn will change depending on level selected
def computerTroopSpawn(computerSpawnLevel, computerSpawnDelayLevel):
    global computerSpawn
    global nextSpawn
    global key7
    global key8
    global key9
    global key0

    # nextSpawn is the dealy in frames of when computer will spawn the next troop
    try:
        # spawn troops
        if nextSpawn == 0:

            # gets random int that coorespond to key7, key8, key9, key0
            resetComputerSpawn()
            computerSpawn = computerSpawnLevel

            if computerSpawn == 1:
                key7 = True
            elif computerSpawn == 2:
                key8 = True
            elif computerSpawn == 3:
                key9 = True
            elif computerSpawn == 4:
                key0 = True

            resetComputerSpawnDelay()
            nextSpawn = computerSpawnDelayLevel

        else:
            nextSpawn -= 1

    except:
        pass


# reset difficulty variables (level1ComputerSpawn, level1ComputerSpawnDelay) so that they change each time
def resetComputerSpawn():
    global level1ComputerSpawn
    global level2ComputerSpawn
    global level3ComputerSpawn


    level1ComputerSpawn = random.randint(0, 2)
    level2ComputerSpawn = random.randint(0, 3)
    level3ComputerSpawn = random.randint(0, 4)


def resetComputerSpawnDelay():
    global level1ComputerSpawnDelay
    global level2ComputerSpawnDelay
    global level3ComputerSpawnDelay

    level1ComputerSpawnDelay = random.randint(60, 90)
    level2ComputerSpawnDelay = random.randint(30, 60)
    level3ComputerSpawnDelay = random.randint(10, 30)


# end game after one tower is destroyed
def endGame(player, player1, player2):
    global menu
    global setting
    global singlePlayer
    global multiplayer
    global levelSelection
    global player1Win
    global player2Win
    global singleWin
    global singleLose

    if len(player) == 0:
        menu = True
        setting = False
        singlePlayer = False
        multiplayer = False
        levelSelection = False
        singleWin = False
        singleLose = False
        player1Win = player1
        player2Win = player2


def singleEndGame(player, player1, player2):
    global menu
    global setting
    global singlePlayer
    global multiplayer
    global levelSelection
    global player1Win
    global player2Win
    global singleWin
    global singleLose

    if len(player) == 0:
        menu = True
        setting = False
        singlePlayer = False
        multiplayer = False
        levelSelection = False
        singleWin = player1
        singleLose = player2
        player1Win = False
        player2Win = False


# reset everything after the game end to prepare for next game
def resetAll():
    global player1TroopNumList
    global player1TroopTypeList
    global player1TroopStateList
    global player1TroopXList
    global player1TroopYList
    global player1TroopHealthList

    global player2TroopNumList
    global player2TroopTypeList
    global player2TroopStateList
    global player2TroopXList
    global player2TroopYList
    global player2TroopHealthList

    global nextSpawn
    global nextSpawnFrame
    global computerSpawn

    global player1Tower
    global player2Tower

    global player1Mana
    global player2Mana

    global giveStartingMana

    global player1FirstTroop
    global player2FirstTroop

    global player1FirstTroopIndex
    global player2FirstTroopIndex

    global mapRealitiveX
    global setLevel

    player1TroopNumList = []
    player1TroopTypeList = []
    player1TroopStateList = []
    player1TroopXList = []
    player1TroopYList = []
    player1TroopHealthList = []

    player2TroopNumList = []
    player2TroopTypeList = []
    player2TroopStateList = []
    player2TroopXList = []
    player2TroopYList = []
    player2TroopHealthList = []

    nextSpawn = 0
    nextSpawnFrame = 0
    computerSpawn = False

    player1Tower = True
    player2Tower = True

    player1Mana = 0
    player2Mana = 0

    giveStartingMana = True

    player1FirstTroop = False
    player2FirstTroop = False

    player1FirstTroopIndex = False
    player2FirstTroopIndex = False

    mapRealitiveX = 0
    setLevel = True


# function for buttons on the game over screen
def singleGameOverButton(x1, x2, y1, y2, open, close):
    global singleWin
    global singleLose
    global singlePlayer
    global menu
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:
            singleWin = False
            singleLose = False
            singlePlayer = open
            menu = close


def multiGameOverButton(x1, x2, y1, y2, open, close):
    global player1Win
    global player2Win
    global multiplayer
    global menu
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]

    if event.type == pygame.MOUSEBUTTONDOWN:
        if x1 < mouseX < x2 and y1 < mouseY < y2:
            player1Win = False
            player2Win = False
            multiplayer = open
            menu = close


# function to change map, x position of map, tower, and troops depending on map/level
def resetMap(num, pic):
    global setLevel
    global background
    global backgroundXY
    global player1TowerX
    global player2TowerX
    global player2SwordManX
    global player2BombManX
    global player2FireDragonX
    global player2HellSnakeX

    if (level is num and setLevel) or (multiplayer is True and setLevel):
        setLevel = False
        background = pygame.image.load(pic).convert_alpha()
        backgroundXY = background.get_rect()
        player1TowerX = backgroundXY[0] + 20 + mapRealitiveX
        player2TowerX = backgroundXY[2] - 200 + mapRealitiveX
        player2SwordManX = backgroundXY[2] - 220 + mapRealitiveX
        player2BombManX = backgroundXY[2] - 220 + mapRealitiveX
        player2FireDragonX = backgroundXY[2] - 220 + mapRealitiveX
        player2HellSnakeX = backgroundXY[2] - 220 + mapRealitiveX


menu = True
resetKeys()

# -----------------------------------------------------------------------------------------------------------------------
# start of program


# loops whole program
while inPlay:

    while menu:

        mainMenu()

        for event in pygame.event.get():
            mouseDown()

            exitKey()
            # open single player level selection
            mouseMainMenuSingle(440, 760, 350, 420)
            # open multiplayer
            mouseMainMenuMulti(440, 760, 435, 510)
            # open setting
            mouseSetting(540, 660, 530, 650, False, True)
            # opens instructions
            mouseInstructions(680, 790, 540, 650, False, True)

        #grid()
        clock.tick(fps)
        pygame.display.update()

    while setting:

        for event in pygame.event.get():

            exitKey()

            # mouseDown()

            # 10 fps
            mouseSettingFPS(580, 650, 370, 430, 10)
            # 30 fps
            mouseSettingFPS(651, 730, 370, 430, 30)
            # 60 fps
            mouseSettingFPS(731, 820, 370, 430, 60)
            # reset troop speeds ratio
            changeTroopSpeedFps()
            # reset window move speed ratio
            changeWindowMoveSpeedFps()
            # closes setting
            mouseSetting(540, 660, 570, 650, True, False)
            # back button
            mouseSetting(410, 520, 540, 650, True, False)

            #when click on setting buttons, change music and sound volume
            mouseSettingBackgroundMusic(580, 650, 210, 280, 0.0)
            mouseSettingBackgroundMusic(651, 730, 210, 280, 0.5)
            mouseSettingBackgroundMusic(731, 820, 210, 280, 1)

            mouseSettingSoundEffect(580, 650, 280, 360, 0.0)
            mouseSettingSoundEffect(651, 730, 280, 360, 0.3)
            mouseSettingSoundEffect(731, 820, 280, 360, 0.6)

        redrawSetting()

        # display selected fps setting
        if fps == 10:
            redrawButton(608, 377)
        if fps == 30:
            redrawButton(681, 377)
        if fps == 60:
            redrawButton(760, 377)

        #display selected background music volume setting
        if musicVolume == 0.0:
            redrawButton(608, 232)
        if musicVolume == 0.5:
            redrawButton(681, 232)
        if musicVolume == 1:
            redrawButton(760, 232)

        #display selected sound effect volume setting
        if soundVolume == 0.0:
            redrawButton(608, 305)
        if soundVolume == 0.3:
            redrawButton(681, 305)
        if soundVolume == 0.6:
            redrawButton(760, 305)


        #grid()
        clock.tick(fps)
        pygame.display.update()


    while levelSelection:

        for event in pygame.event.get():
            exitKey()

            # back button
            mouseBackLevelSelection(410, 520, 540, 650, True, False)

            # level 1
            mousePosition(450, 520, 240, 310)

            # sets diffuculty, opens singleplayer
            # button for level 1
            selectDifficulty(450, 520, 240, 310, 1)

            # level 2
            selectDifficulty(580, 645, 240, 310, 2)

            # level 3
            selectDifficulty(700, 770, 240, 310, 3)

        redrawlevelSelection()

        clock.tick(fps)
        pygame.display.update()

    while instructions:

        for event in pygame.event.get():
            exitKey()

            # click question mark to exit to menu
            mouseInstructions(680, 790, 540, 650, True, False)

            # click back button to exit to menu
            mouseInstructions(410, 520, 540, 650, True, False)

        redrawInstructions()

        clock.tick(fps)
        pygame.display.update()

    while multiplayer:

        resetMap(1, "background.png")

        resetKeys()

        redrawGameWindow()

        # draw ui box
        drawPlayer1UI()

        # troop descriptions
        if mouseHover(30, 110, 530, 590):
            troopDescription(swordManHP, player1SwordmanDamage * fps / 60, player2SwordmanRange, swordManSpeedX,
                             player1SwordmanCost, 280, 540)

        if mouseHover(135, 215, 530, 590):
            troopDescription(bombManHP, player1BombManDamage * fps / 60, player2BombManRange, bombManSpeedX,
                             player1BombManCost, 280, 540)

        if mouseHover(30, 110, 610, 670):
            troopDescription(fireDragonHP, player1DragonDamage * fps / 60, player2DragonRange, fireDragonSpeedX,
                             player1DragonCost, 280, 540)

        if mouseHover(135, 215, 610, 670):
            troopDescription(hellSnakeHP, player1HellSnakeDamage * fps / 60, player2HellSnakeRange, hellSnakeSpeedX,
                             player1HellSnakeCost, 280, 540)

        drawPlayer2UI()

        # troop descriptions
        if mouseHover(630, 710, 530, 590):
            troopDescription(swordManHP, player1SwordmanDamage * fps / 60, player2SwordmanRange, swordManSpeedX,
                             player1SwordmanCost, 880, 540)

        if mouseHover(735, 815, 530, 590):
            troopDescription(bombManHP, player1BombManDamage * fps / 60, player2BombManRange, bombManSpeedX,
                             player1BombManCost, 880, 540)

        if mouseHover(630, 710, 610, 670):
            troopDescription(fireDragonHP, player1DragonDamage * fps / 60, player2DragonRange, fireDragonSpeedX,
                             player1DragonCost, 880, 540)

        if mouseHover(735, 815, 610, 670):
            troopDescription(hellSnakeHP, player1HellSnakeDamage * fps / 60, player2HellSnakeRange, hellSnakeSpeedX,
                             player1HellSnakeCost, 880, 540)

        startingMana(player1StartingMana, player2StartingMana)

        drawPlayer1Mana(player1Mana, 500)

        drawPlayer1Mana(player2Mana, 1100)

        player1AddMana()

        player2AddMana()

        # get mouse inputs
        for event in pygame.event.get():
            exitKey()

            mouseDown()

            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]

            # mouse position for moving the screen
            moveScreen(0, 100, 0, 500)
            moveScreen(1100, 1200, 0, 500)

            # click buttons to deploy player 1 troops
            mousePosition(30, 110, 530, 590)
            mousePosition(135, 215, 530, 590)
            mousePosition(30, 110, 610, 670)
            mousePosition(135, 215, 610, 670)

            # player 2 buttons
            mousePosition(630, 710, 530, 590)
            mousePosition(735, 815, 530, 590)
            mousePosition(630, 710, 610, 670)
            mousePosition(735, 815, 610, 670)

            # see if mouse is hovering over troop selection buttons
            # player1
            mouseHover(30, 110, 530, 590)
            mouseHover(135, 215, 530, 590)
            mouseHover(30, 110, 610, 670)
            mouseHover(135, 215, 610, 670)

            # player2
            mouseHover(630, 710, 530, 590)
            mouseHover(735, 815, 530, 590)
            mouseHover(630, 710, 610, 670)
            mouseHover(735, 815, 610, 670)

        # get keyboard inputs
        pygame.event.get()

        keysPressed()

        moveGameWindow()

        # player 1 deploy troops
        # deploy swordman
        player1DeployTroop(key1, swordMan, "moving", swordManX, swordManY, swordManHP, player1SwordmanCost)

        # deploy bombman
        player1DeployTroop(key2, bombMan, "moving", bombManX, bombManY, bombManHP, player1BombManCost)

        # deploy dragon
        player1DeployTroop(key3, dragon, "moving", fireDragonX, fireDragonY, fireDragonHP, player1DragonCost)

        # deploy snake
        player1DeployTroop(key4, snake, "moving", hellSnakeX, hellSnakeY, hellSnakeHP, player1HellSnakeCost)

        # player 2 deploy troops
        # deploy swordman
        player2DeployTroop(key7, swordMan, "moving", player2SwordManX, swordManY, swordManHP, player2SwordmanCost)

        # deploy bombman
        player2DeployTroop(key8, bombMan, "moving", player2BombManX, bombManY, bombManHP, player2BombManCost)

        # deploy dragon
        player2DeployTroop(key9, dragon, "moving", player2FireDragonX, fireDragonY, fireDragonHP, player2DragonCost)

        # deploy snake
        player2DeployTroop(key0, snake, "moving", player2HellSnakeX, hellSnakeY, hellSnakeHP, player2HellSnakeCost)

        resetMouseDown()

        # find troop to be targeted
        player1Targeted()

        player2Targeted()

        # create Towers (only do this once)
        player1DeployTroop(player1Tower, tower, "null", player1TowerX, player1TowerY, player1TowerHP, 0)
        player1Tower = False

        player2DeployTroop(player2Tower, tower, "null", player2TowerX, player2TowerY, player2TowerHP, 0)
        player2Tower = False

        # cycles through list of troops for player 1
        for player1NumTroop in range(len(player1TroopTypeList)):
            # sword man
            player1AnnimateAndMoveTroops("swordMan", player1SwordmanRange, swordManSpeedX, swordManPic, swordManY)
            player1SoundEffect("swordMan")

            # bomb man
            player1AnnimateAndMoveTroops("bombMan", player1BombManRange, bombManSpeedX, bombManPic, bombManY)
            player1SoundEffect("bombMan")

            # dragon
            player1AnnimateAndMoveTroops("dragon", player1DragonRange, fireDragonSpeedX, fireDragonPic, fireDragonY)
            player1SoundEffect("dragon")

            # snake
            player1AnnimateAndMoveTroops("snake", player1HellSnakeRange, hellSnakeSpeedX, hellSnakePic, hellSnakeY)
            player1SoundEffect("snake")

        # cycles through list of troops for player 2
        for player2NumTroop in range(len(player2TroopTypeList)):
            # swordman
            player2AnnimateAndMoveTroops("swordMan", player2SwordmanRange, swordManSpeedX, player2SwordManPic,
                                         swordManY)
            player2SoundEffect("swordMan")
            # bomb man
            player2AnnimateAndMoveTroops("bombMan", player2BombManRange, bombManSpeedX, player2BombManPic, bombManY)
            player2SoundEffect("bombMan")
            # dragon
            player2AnnimateAndMoveTroops("dragon", player2DragonRange, fireDragonSpeedX, player2FireDragonPic,
                                         fireDragonY)
            player2SoundEffect("dragon")
            # snake
            player2AnnimateAndMoveTroops("snake", player2HellSnakeRange, hellSnakeSpeedX, player2HellSnakePic,
                                         hellSnakeY)
            player2SoundEffect("snake")

        # remove troops after they die
        removeTroops(player1FirstTroopIndex, player1TroopHealthList, player1TroopTypeList, player1TroopStateList,
                     player1TroopXList, player1TroopYList)

        removeTroops(player2FirstTroopIndex, player2TroopHealthList, player2TroopTypeList, player2TroopStateList,
                     player2TroopXList, player2TroopYList)

        drawAllyTower()

        drawEnemyTower()

        # grid()

        # realFrame is when inPlay loops once, 1 realFrame = 1 loop
        # mana, move screen, and UI are tied to realFrame
        # frame is displaying troops animation, 1 frame = 1 sprite
        realFrame += 1
        if realFrame % (fps / 10) == 0:
            frame += 1

        # end game when one tower is destroyed
        # open player1 / player2 win screen
        endGame(player1TroopTypeList, False, True)
        endGame(player2TroopTypeList, True, False)

        clock.tick(fps)
        # print(clock.get_fps())
        pygame.display.update()
        pygame.display.update()

    while singlePlayer:

        # change map depending on level
        # (only do this once)
        resetMap(1, "background3.png")

        resetMap(2, "background4.png")

        resetMap(3, "background5.png")

        resetKeys()

        redrawGameWindow()

        startingMana(player1StartingMana, 0)

        drawsinglePlayerUI()

        drawLevel()

        # troop descriptions
        if mouseHover(30, 110, 530, 590):
            troopDescription(swordManHP, player1SwordmanDamage, player2SwordmanRange, swordManSpeedX,
                             player1SwordmanCost, 280, 540)

        if mouseHover(135, 215, 530, 590):
            troopDescription(bombManHP, player1BombManDamage, player2BombManRange, bombManSpeedX, player1BombManCost,
                             280, 540)

        if mouseHover(30, 110, 610, 670):
            troopDescription(fireDragonHP, player1DragonDamage, player2DragonRange, fireDragonSpeedX, player1DragonCost,
                             280, 540)

        if mouseHover(135, 215, 610, 670):
            troopDescription(hellSnakeHP, player1HellSnakeDamage, player2HellSnakeRange, hellSnakeSpeedX,
                             player1HellSnakeCost, 280, 540)

        drawPlayer1Mana(player1Mana, 500)

        player1AddMana()

        # get mouse inputs
        for event in pygame.event.get():
            exitKey()

            mouseDown()

            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]

            # mouse position for moving the screen
            moveScreen(0, 100, 0, 500)
            moveScreen(1100, 1200, 0, 500)

            # click buttons to deploy player 1 troops
            mousePosition(30, 110, 530, 590)
            mousePosition(135, 215, 530, 590)
            mousePosition(30, 110, 610, 670)
            mousePosition(135, 215, 610, 670)

            # see if mouse is hovering over troop selection buttons
            mouseHover(30, 110, 530, 590)
            mouseHover(135, 215, 530, 590)
            mouseHover(30, 110, 610, 670)
            mouseHover(135, 215, 610, 670)

            # back button that goes to main menu
            mouseBackSinglePlayer(1060, 1170, 560, 650)

        # get keyboard events
        pygame.event.get()

        keysPressed()

        moveGameWindow()

        # set diffuculty depending on level
        if level == 1:
            computerTroopSpawn(level1ComputerSpawn, level1ComputerSpawnDelay)

        if level == 2:
            computerTroopSpawn(level2ComputerSpawn, level2ComputerSpawnDelay)

        if level == 3:
            computerTroopSpawn(level3ComputerSpawn, level3ComputerSpawnDelay)

        # player 1 deploy troops
        # deploy swordman
        player1DeployTroop(key1, swordMan, "moving", swordManX, swordManY, swordManHP, player1SwordmanCost)

        # deploy bombman
        player1DeployTroop(key2, bombMan, "moving", bombManX, bombManY, bombManHP, player1BombManCost)

        # deploy dragon
        player1DeployTroop(key3, dragon, "moving", fireDragonX, fireDragonY, fireDragonHP, player1DragonCost)

        # deploy snake
        player1DeployTroop(key4, snake, "moving", hellSnakeX, hellSnakeY, hellSnakeHP, player1HellSnakeCost)

        # player 2 deploy troops
        # deploy swordman
        computerDeployTroop(key7, swordMan, "moving", player2SwordManX, swordManY, swordManHP)

        # deploy bombman
        computerDeployTroop(key8, bombMan, "moving", player2BombManX, bombManY, bombManHP)

        # deploy dragon
        computerDeployTroop(key9, dragon, "moving", player2FireDragonX, fireDragonY, fireDragonHP)

        # deploy snake
        computerDeployTroop(key0, snake, "moving", player2HellSnakeX, hellSnakeY, hellSnakeHP)

        resetMouseDown()

        # find troop to be targeted
        player1Targeted()

        player2Targeted()

        # create Towers (only do this once)
        player1DeployTroop(player1Tower, tower, "null", player1TowerX, player1TowerY, player1TowerHP, 0)
        player1Tower = False

        player2DeployTroop(player2Tower, tower, "null", player2TowerX, player2TowerY, player2TowerHP, 0)
        player2Tower = False

        # cycles through list of troops for player 1
        for player1NumTroop in range(len(player1TroopTypeList)):
            # sword man
            player1AnnimateAndMoveTroops("swordMan", player1SwordmanRange, swordManSpeedX, swordManPic, swordManY)
            player1SoundEffect("swordMan")

            # bomb man
            player1AnnimateAndMoveTroops("bombMan", player1BombManRange, bombManSpeedX, bombManPic, bombManY)
            player1SoundEffect("bombMan")

            # dragon
            player1AnnimateAndMoveTroops("dragon", player1DragonRange, fireDragonSpeedX, fireDragonPic, fireDragonY)
            player1SoundEffect("dragon")

            # snake
            player1AnnimateAndMoveTroops("snake", player1HellSnakeRange, hellSnakeSpeedX, hellSnakePic, hellSnakeY)
            player1SoundEffect("snake")

        # cycles through list of troops for player 2
        for player2NumTroop in range(len(player2TroopTypeList)):
            # swordman
            player2AnnimateAndMoveTroops("swordMan", player2SwordmanRange, swordManSpeedX, player2SwordManPic,
                                         swordManY)
            player2SoundEffect("swordMan")
            # bomb man
            player2AnnimateAndMoveTroops("bombMan", player2BombManRange, bombManSpeedX, player2BombManPic, bombManY)
            player2SoundEffect("bombMan")

            # dragon
            player2AnnimateAndMoveTroops("dragon", player2DragonRange, fireDragonSpeedX, player2FireDragonPic,
                                         fireDragonY)
            player2SoundEffect("dragon")

            # snake
            player2AnnimateAndMoveTroops("snake", player2HellSnakeRange, hellSnakeSpeedX, player2HellSnakePic,
                                         hellSnakeY)
            player2SoundEffect("snake")

        # remove troops after they die
        removeTroops(player1FirstTroopIndex, player1TroopHealthList, player1TroopTypeList, player1TroopStateList,
                     player1TroopXList, player1TroopYList)

        removeTroops(player2FirstTroopIndex, player2TroopHealthList, player2TroopTypeList, player2TroopStateList,
                     player2TroopXList, player2TroopYList)

        drawAllyTower()

        drawEnemyTower()

        realFrame += 1
        if realFrame % (fps / 10) == 0:
            frame += 1

        # end game when one tower is destroyed
        singleEndGame(player1TroopTypeList, False, True)
        singleEndGame(player2TroopTypeList, True, False)

        # grid()
        clock.tick(fps)
        # print(clock.get_fps())
        # print fps
        pygame.display.update()

    while player1Win:

        for event in pygame.event.get():
            exitKey()
            resetAll()

            multiGameOverButton(650, 735, 320, 435, True, False)
            multiGameOverButton(470, 575, 335, 435, False, True)

        redrawPlayer1Win()

        # print "menu", menu
        # print "player1WinPic", player1Win

        # grid()
        # print(clock.get_fps())
        clock.tick(fps)
        pygame.display.update()

    while player2Win:
        for event in pygame.event.get():
            exitKey()
            resetAll()

            multiGameOverButton(650, 735, 320, 435, True, False)
            multiGameOverButton(470, 575, 335, 435, False, True)

        redrawPlayer2Win()

        # grid()
        #print(clock.get_fps())
        clock.tick(fps)
        pygame.display.update()

    while singleWin:
        for event in pygame.event.get():
            exitKey()
            resetAll()

            singleGameOverButton(650, 735, 320, 435, True, False)
            singleGameOverButton(470, 575, 335, 435, False, True)

        redrawSingleWin()

        clock.tick(fps)
        pygame.display.update()

    while singleLose:
        for event in pygame.event.get():
            exitKey()
            resetAll()

            singleGameOverButton(650, 735, 320, 435, True, False)
            singleGameOverButton(470, 575, 335, 435, False, True)

        redrawSingleLose()

        # grid()
        clock.tick(fps)
        pygame.display.update()

pygame.quit()

"""
important to do

- make everything on screen realitive to background x and y
- make all characters in a list
- loop through list, if troop state = false/dead, remove troop from list
- use map.get_rect() to get dimensions of the map
    - make towers and troop spawn at eg. left side of map + 100, right side of map - 100
- 1 list for troops
- make function with different prarmeters for deploying troops
- troops need to scan for enemies in front
    - if enemies in front, state change from moveing to attacking
  
- create 1 function for deploying troops
- create 1 finction for animating troops
- create 1 function for everything 


- when deployig troops, make y position random/ vaired so some troops in front, some in back. 



- CREATE STARTING MENU
- create ui 
- game over screen

- need function to reset multiplayer/singleplayer
    - reset all variables
    
    
- need to add

- music
- sound
- game over screen
    - include restart button
    - back to main menu button
    - reset all variables 
    
DONE- troop description 
    - if mouse hovers over button, show description 
    
DONE- music sound settings 
DONE- backbutton in game


 
"""
