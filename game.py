#########################################
# File Name: ToonyWars.py
# Description: Game
# Author: Jonathan Yam, Leo
# Date: 11/29/2018
#########################################
import pygame
import math
from random import randint 

pi = math.pi
pygame.init()
WIDTH = 1200
HEIGHT= 700
TOP = 0
BOTTOM = 640
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

BLACK = (0,0,0)
RED  =(255,  0,  0)
YELLOW=(255,255,0)
ORANGE = (255,128,64)
GREEN=(  0,128,  0)
BLUE =(0,255,255)
WHITE=(255,255,255)
GREY=(72,72,72)
BROWN =(185,122,87)
outline=0


#Tower Properties
allyTowerPic = pygame.image.load("tower1.png")
enemyTowerPic = pygame.image.load("tower2.png")
allyTowerX = 20
allyTowerY = BOTTOM-300
enemyTowerX = 1000
enemyTowerY = BOTTOM-300
allyTowerVisible = True
enemyTowerVisible = True
allyTowerHP = 100000
enemyTowerHP = 5000

#Sword Man Properties
numOfSwordManPics = 6
swordManPic = []
for i in range(numOfSwordManPics):
    swordManPic.append(pygame.image.load("swordman"+str(i)+".png"))
numberOfSwordMan = 100
swordManPicNum = []
swordManX = []
swordManY = []
swordManSpeedX = []
swordManHP = []
swordManW = 130
swordManH = 130
swordManVisible = []
for i in range(numberOfSwordMan):
    swordManPicNum.append(0)
    swordManX.append(100)
    swordManY.append(500)
    swordManSpeedX.append(5)
    swordManHP.append(1000)
    swordManVisible.append(False)

#Sword Man Properties
numOfFireDragonPics = 6
fireDragonPic = []
for i in range(numOfFireDragonPics):
    fireDragonPic.append(pygame.image.load("dragon"+str(i)+".png"))
fireDragonPicNum = 0
fireDragonX = 700
fireDragonY = 400
fireDragonSpeedX = -6
fireDragonHP = 200000
fireDragonW = 130
fireDragonH = 130
fireDragonVisible = True

#---------------------------------------#
# the main program begins here          #
#---------------------------------------#


background = pygame.image.load("background.jpg")
font1 = pygame.font.SysFont("ALGERIAN",10)
font2 = pygame.font.SysFont("ALGERIAN",20)

backgroundX = 0 
backgroundY = 0
letterX=320	                        
letterY=240

#flag to close program when hit escape key
inPlay = True
gameOver = False

def initSwordMan(i):
    global swordManPicNum
    global swordManX
    global swordManY
    global swordManSpeedX
    global swordManHP
    global swordManVisible
    
    swordManPicNum[i] = 0
    swordManX[i] = 100
    swordManY[i] = 500
    swordManSpeedX[i] = 5
    swordManHP[i] = 1000
    swordManVisible[i] = True

def initFireDragon():
    global fireDragonPicNum
    global fireDragonX
    global fireDragonY
    global fireDragonSpeedX
    global fireDragonHP      
    global fireDragonVisible
    
    fireDragonPicNum = 0
    fireDragonX = 700
    fireDragonY = 400
    fireDragonSpeedX = -6
    fireDragonHP = 2000        
    fireDragonVisible = True
    return

def redrawGameWindow():
    global numberOfSwordMan
    
    #draw background
    gameWindow.fill(WHITE)
    gameWindow.blit(background, (backgroundX,backgroundY))
    if (allyTowerVisible):
        gameWindow.blit(allyTowerPic, (allyTowerX,allyTowerY))
        letterGraphics = font2.render("HP: " +str(allyTowerHP),1,BLACK)
        gameWindow.blit(letterGraphics, (50,50))
    if (enemyTowerVisible):
        gameWindow.blit(enemyTowerPic, (enemyTowerX,enemyTowerY))
        letterGraphics = font2.render("HP: " +str(enemyTowerHP),1,BLACK)
        gameWindow.blit(letterGraphics, (1050,50))
    for i in range(numberOfSwordMan):
        if (swordManVisible[i]):
            gameWindow.blit(swordManPic[swordManPicNum[i]], (swordManX[i],swordManY[i]))
            letterGraphics = font1.render("HP: " +str(swordManHP[i]),1,BLACK)
            gameWindow.blit(letterGraphics, (swordManX[i], BOTTOM+20))
        
    #Draw Dragon 
    if (fireDragonVisible):
        gameWindow.blit(fireDragonPic[fireDragonPicNum], (fireDragonX,fireDragonY))
        letterGraphics = font1.render("HP: " +str(fireDragonHP),1,BLACK)
        gameWindow.blit(letterGraphics, (fireDragonX, BOTTOM+40))
    return

def runGame():
    return

        
    

#loops whole program
while inPlay:

    redrawGameWindow()
    pygame.display.update()
    clock.tick(10)
    print clock

    
    pygame.event.get()                  # check for any events
    keys = pygame.key.get_pressed()     # get_pressed() method generates a True/False list for the status of all keys
    if keys[pygame.K_ESCAPE]:           # if ESC has been pressed exit from the game
        inPlay = False
    elif keys[pygame.K_1]:
        for i in range(numberOfSwordMan):
            if swordManVisible[i] == False:
                initSwordMan(i)
                break
                
            

    runGame()
    
    for i in range(numberOfSwordMan):
        if (swordManHP[i] > 0):
            if (enemyTowerHP > 0 and swordManX[i]+swordManW > enemyTowerX):
                enemyTowerHP -= 100
                swordManSpeedX[i] = 0
                swordManPicNum[i] = (swordManPicNum[i] + 1)%3
            elif (fireDragonHP > 0 and swordManX[i]+swordManW > fireDragonX + 80):
                fireDragonHP -= 1
                swordManSpeedX[i] = 0
                swordManPicNum[i] = (swordManPicNum[i] + 1)%3
            else:
                swordManSpeedX[i] = 5
                swordManX[i] = swordManX[i] + swordManSpeedX[i] 
                swordManPicNum[i] = (swordManPicNum[i] + 1)%3 + 3
            
    #dragon
    if (fireDragonHP > 0):
        fireDragonFighting = False
        for i in range(numberOfSwordMan):
            if (swordManHP[i] > 0 and fireDragonX < swordManX[i]+swordManW):
                swordManHP[i] -= 10
                fireDragonFighting = True;
            
        if (allyTowerHP > 0 and fireDragonX < allyTowerX):
            allyTowerHP -= 50
            fireDragonSpeedX = 0
            fireDragonPicNum = (fireDragonPicNum + 1)%3 + 3  # fighting
        elif (fireDragonFighting == True):
            fireDragonSpeedX = 0
            fireDragonPicNum = (fireDragonPicNum + 1)%3 + 3  # fighting
        else:
            fireDragonSpeedX = -6
            fireDragonX = fireDragonX + fireDragonSpeedX 
            fireDragonPicNum = (fireDragonPicNum + 1)%3   # standing

    if (allyTowerHP <= 0):
        allyTowerVisible = False
    if (enemyTowerHP <= 0):
        enemyTowerVisible = False
        fireDragonVisible = False

    for i in range(numberOfSwordMan):        
        if (swordManHP[i] <= 0):
            swordManVisible[i] = False
    if (fireDragonHP <= 0 and enemyTowerHP > 0):
        fireDragonVisible = False
        n = randint(1, 100) 
        if n % 13 == 0:
            initFireDragon()
        

    

    
pygame.quit()



    
   

    









    


