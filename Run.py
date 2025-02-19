# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:05:37 2018

@author: Andy
"""

import pygame, sys, random
import time
pygame.init()
screen=pygame.display.set_mode([800,600])
screen.fill([255,255,255])
t=2
i=0
running=True
while running:
    pygame.draw.lines(screen,[0,0,0],False,[[0,400],[800,400]],1)
    pygame.draw.rect(screen,[255,0,0],[300,380,20,20],0)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                t=0
            elif event.key==pygame.K_DOWN:
                t=1
    pygame.time.delay(100)
    if t==0:
        pygame.draw.rect(screen,[255,0,0],[300,360,20,20],0)
        pygame.draw.rect(screen,[255,255,255],[300,380,20,20],0)
        time.sleep(2)
        running=False
    elif t==1:
        pygame.draw.rect(screen,[255,255,255],[300,380,20,10],0)
        pygame.time.delay(100)
        pygame.draw.rect(screen,[255,0,0],[300,380,20,20],0)
    pygame.display.flip()     
pygame.quit()
    
        
        