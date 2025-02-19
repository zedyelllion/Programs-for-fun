# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:47:35 2018

@author: Andy Liang
"""

import pygame, sys, random
def drawText(text,posx,posy,textHeight=18,fontColor=(0,0,0),backgroudColor=(255,255,255)):
        fontObj = pygame.font.Font('c:\\windows\\fonts\\ALGER.ttf', textHeight)  
        textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)  
        textRectObj = textSurfaceObj.get_rect()  
        textRectObj.center = (posx, posy)  
        screen.blit(textSurfaceObj, textRectObj)  
        
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([800,600])
screen.fill([255,255,255]) 
pygame.time.delay(1000) 
x=2
y=2
reda=[30,40,50,60,70,80]
redb=[20,20,20,20,20,20]
greena=[30,40,50,60,70,80]
greenb=[120,120,120,120,120,120]
lred=6
lgreen=6
m=True
running=True
while running:
    lred=len(reda)
    drawText("Red:"+str(5*lred),700,50)
    lgreen=len(greena)
    drawText("Green:"+str(5*lgreen),700,100)
    if m:
        x=random.randint(3,77)
        y=random.randint(3,57)
        pygame.draw.rect(screen,[0,0,255],[10*x,10*y,10,10],0)
        m=not m

    for i in range(lred):
        pygame.draw.rect(screen,[255,0,0],[reda[i],redb[i],10,10],0)
    pygame.draw.rect(screen,[255,255,255],[reda[0],redb[0],10,10],0)
    for i in range(lgreen):
        pygame.draw.rect(screen,[0,255,0],[greena[i],greenb[i],10,10],0)
    pygame.draw.rect(screen,[255,255,255],[greena[0],greenb[0],10,10],0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w and redb[lred-1]-redb[lred-2]<=0:
                x=0
            elif event.key==pygame.K_s and redb[lred-1]-redb[lred-2]>=0:
                x=1
            elif event.key==pygame.K_d and reda[lred-1]-reda[lred-2]>=0:
                x=2
            elif event.key==pygame.K_a and reda[lred-1]-reda[lred-2]<=0:
                x=3
            elif event.key==pygame.K_i and greenb[lgreen-1]-greenb[lgreen-2]<=0:
                y=0
            elif event.key==pygame.K_k and greenb[lgreen-1]-greenb[lgreen-2]>=0:
                y=1
            elif event.key==pygame.K_l and greena[lgreen-1]-greena[lgreen-2]>=0:
                y=2
            elif event.key==pygame.K_j and greena[lgreen-1]-greena[lgreen-2]<=0:
                y=3
    if x==0:
        reda.append(reda[lred-1])
        redb.append(redb[lred-1]-10)
        if reda[lred-1]==10*x and redb[lred-1]==10*y+10:
            m=not m
        else:
            del reda[0]
            del redb[0]
        if redb[lred-1]==0:
            running=False
    elif x==1:
        reda.append(reda[lred-1])
        redb.append(redb[lred-1]+10)
        if reda[lred-1]==10*x and redb[lred-1]==10*y-10:
            m=not m
        else:
            del reda[0]
            del redb[0]
        if redb[lred-1]==600:
            running=False
    elif x==2:
        reda.append(reda[lred-1]+10)
        redb.append(redb[lred-1])
        if reda[lred-1]==10*x-10 and redb[lred-1]==10*y+10:
            m=not m
        else:
            del reda[0]
            del redb[0]
        if reda[lred-1]==800:
            running=False
    elif x==3:
        reda.append(reda[lred-1]-10)
        redb.append(redb[lred-1])
        if reda[lred-1]==10*x+10 and redb[lred-1]==10*y+10:
            m=not m
        else:
            del reda[0]
            del redb[0]
        if reda[lred-1]==0:
            running=False
    

    if y==0:
        greena.append(greena[lgreen-1])
        greenb.append(greenb[lgreen-1]-10)
        if greena[lgreen-1]==10*x and greenb[lgreen-1]==10*y+10:
            m=not m
        else:
            del greena[0]
            del greenb[0]
        if greenb[lgreen-1]==0:
            running=False
    elif y==1:
        greena.append(greena[lgreen-1])
        greenb.append(greenb[lgreen-1]+10)
        if greena[lgreen-1]==10*x and greenb[lgreen-1]==10*y-10:
            m=not m
        else:
            del greena[0]
            del greenb[0]
        if greenb[lgreen-1]==600:
            running=False
    elif y==2:
        greena.append(greena[lgreen-1]+10)
        greenb.append(greenb[lgreen-1])
        if greena[lgreen-1]==10*x-10 and greenb[lgreen-1]==10*y: 
            m=not m
        else:
            del greena[0]
            del greenb[0]
        if greena[lgreen-1]==800:
            running=False
    elif y==3:
        greena.append(greena[lgreen-1]-10)
        greenb.append(greenb[lgreen-1])
        if greena[lgreen-1]==10*x+10 and greenb[lgreen-1]==10*y:
            m=not m
        else:
            del greena[0]
            del greenb[0]
        if greena[lgreen-1]==0:
            running=False
    for i in range(1,lred):
        if greena[lgreen-1]==reda[i] and greenb[lgreen-1]==redb[i]:
            running=False
            print("Red won!")
        elif greena[lgreen-1]==reda[i] and greenb[lgreen-1]==redb[i]:
            running=False
            print("Red won!")
        elif greenb[lgreen-1]==redb[i] and greena[lgreen-1]==reda[i]:
            running=False
            print("Red won!")
        elif greenb[lgreen-1]==redb[i] and greena[lgreen-1]==reda[i]:
            running=False
            print("Red won!")
    for i in range(1,lgreen):
        if reda[lred-1]==greena[i] and redb[lred-1]==greenb[i]:
            running=False
            print("Green won!")
        elif reda[lred-1]==greena[i] and redb[lred-1]==greenb[i]:
            running=False
            print("Green won!")
        elif redb[lred-1]==greenb[i] and reda[lred-1]==greena[i]:
            running=False
            print("Green won!")
        elif redb[lred-1]==greenb[i] and reda[lred-1]==greena[i]:
            running=False
            print("Green won!")
            
      
    pygame.time.delay(70)
    
        
    
    
    pygame.display.flip()     
pygame.quit()