# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 16:47:35 2018

@author: lhl
"""

import pygame, sys, random
def drawText(text,posx,posy,textHeight=18,fontColor=(0,0,0),backgroudColor=(255,255,255)):
        fontObj = pygame.font.Font('c:\\windows\\fonts\\ALGER.ttf', textHeight)  # 通过字体文件获得字体对象
        textSurfaceObj = fontObj.render(text, True,fontColor,backgroudColor)  # 配置要显示的文字
        textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
        textRectObj.center = (posx, posy)  # 设置显示对象的坐标
        screen.blit(textSurfaceObj, textRectObj)  # 绘制字
        
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([800,600])
screen.fill([255,255,255]) 
pygame.time.delay(1000) #建立背景
redx=[30,40,50,60,70,80]
redy=[20,20,20,20,20,20]
greenx=[30,40,50,60,70,80]
greeny=[120,120,120,120,120,120]
x=2
y=4
m=True
running=True
while running:
    lred=len(redx)
    drawText("Red:"+str(5*lred),700,50)
    lgreen=len(greenx)
    drawText("Green:"+str(5*lgreen),700,100)
    if m:
        foodx=random.randint(3,77)
        foody=random.randint(3,57)
        pygame.draw.rect(screen,[0,0,255],[10*foodx,10*foody,10,10],0)
        m=not m

    
    for i in range(lred):
        pygame.draw.rect(screen,[255,0,0],[redx[i],redy[i],10,10],0)
    pygame.draw.rect(screen,[255,255,255],[redx[0],redy[0],10,10],0)
    for i in range(lgreen):
        pygame.draw.rect(screen,[0,255,0],[greenx[i],greeny[i],10,10],0)
    pygame.draw.rect(screen,[255,255,255],[greenx[0],greeny[0],10,10],0)
   
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w and redy[lred-1]-redy[lred-2]<=0:
                x=0
            elif event.key==pygame.K_s and redy[lred-1]-redy[lred-2]>=0:
                x=1
            elif event.key==pygame.K_d and redx[lred-1]-redx[lred-2]>=0:
                x=2
            elif event.key==pygame.K_a and redx[lred-1]-redx[lred-2]<=0:
                x=3
            elif event.key==pygame.K_i and greeny[lgreen-1]-greeny[lgreen-2]<=0:
                y=0
            elif event.key==pygame.K_k and greeny[lgreen-1]-greeny[lgreen-2]>=0:
                y=1
            elif event.key==pygame.K_l and greenx[lgreen-1]-greenx[lgreen-2]>=0:
                y=2
            elif event.key==pygame.K_j and greenx[lgreen-1]-greenx[lgreen-2]<=0:
                y=3
    
    
    if x==0:
        redx.append(redx[lred-1])
        redy.append(redy[lred-1]-10)
        if redx[lred-1]==10*foodx and redy[lred-1]==10*foody:
            m=not m
        else:
            del redx[0]
            del redy[0]
        if redy[lred-1]==0:
            running=False
    elif x==1:
        redx.append(redx[lred-1])
        redy.append(redy[lred-1]+10)
        if redx[lred-1]==10*foodx and redy[lred-1]==10*foody:
            m=not m
        else:
            del redx[0]
            del redy[0]
        if redy[lred-1]==600:
            running=False
    elif x==2:
        redx.append(redx[lred-1]+10)
        redy.append(redy[lred-1])
        if redx[lred-1]==10*foodx and redy[lred-1]==10*foody:
            m=not m
        else:
            del redx[0]
            del redy[0]
        if redx[lred-1]==800:
            running=False
    elif x==3:
        redx.append(redx[lred-1]-10)
        redy.append(redy[lred-1])
        if redx[lred-1]==10*foodx and redy[lred-1]==10*foody:
            m=not m
        else:
            del redx[0]
            del redy[0]
        if redx[lred-1]==0:
            running=False
    
    

    if y==0:
        greenx.append(greenx[lgreen-1])
        greeny.append(greeny[lgreen-1]-10)
        if greenx[lgreen-1]==10*foodx and greeny[lgreen-1]==10*foody:
            m=not m
        else:
            del greenx[0]
            del greeny[0]
        if greeny[lgreen-1]==0:
            running=False
    elif y==1:
        greenx.append(greenx[lgreen-1])
        greeny.append(greeny[lgreen-1]+10)
        if greenx[lgreen-1]==10*foodx and greeny[lgreen-1]==10*foody:
            m=not m
        else:
            del greenx[0]
            del greeny[0]
        if greeny[lgreen-1]==600:
            running=False
    elif y==2:
        greenx.append(greenx[lgreen-1]+10)
        greeny.append(greeny[lgreen-1])
        if greenx[lgreen-1]==10*foodx and greeny[lgreen-1]==10*foody:
            m=not m
        else:
            del greenx[0]
            del greeny[0]
        if greenx[lgreen-1]==800:
            running=False
    elif y==3:
        greenx.append(greenx[lgreen-1]-10)
        greeny.append(greeny[lgreen-1])
        if greenx[lgreen-1]==10*foodx and greeny[lgreen-1]==10*foody:
            m=not m
        else:
            del greenx[0]
            del greeny[0]
        if greenx[lgreen-1]==0:
            running=False
    
    
    
    for i in range(1,lred):
        if greenx[lgreen-1]==redx[i] and greeny[lgreen-1]==redy[i]:
            running=False
            print("Red won!")
        elif greenx[lgreen-1]==redx[i] and greeny[lgreen-1]==redy[i]:
            running=False
            print("Red won!")
        elif greeny[lgreen-1]==redy[i] and greenx[lgreen-1]==redx[i]:
            running=False
            print("Red won!")
        elif greeny[lgreen-1]==redy[i] and greenx[lgreen-1]==redx[i]:
            running=False
            print("Red won!")
    
    
    for i in range(1,lgreen):
        if redx[lred-1]==greenx[i] and redy[lred-1]==greeny[i]:
            running=False
            print("Green won!")
        elif redx[lred-1]==greenx[i] and redy[lred-1]==greeny[i]:
            running=False
            print("Green won!")
        elif redy[lred-1]==greeny[i] and redx[lred-1]==greenx[i]:
            running=False
            print("Green won!")
        elif redy[lred-1]==greeny[i] and redx[lred-1]==greenx[i]:
            running=False
            print("Green won!")
            
      
    pygame.time.delay(70)
    
        
    
    
    pygame.display.flip()     
pygame.quit()