# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 21:29:22 2019

@author: Andy Liang
"""

import pygame, sys
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode([800,800])
screen.fill([180,180,180]) 
running=True
steps=0
black=[]
white=[]
dots=[]#
adots=[]#

def reaarange(t,steps):
    if steps%2==0:
        h=[]
        other=[]
        a=[t]
        for i in black:
            other.append(i)
        for i in range(0,len(black)):
            x=0
            for j in black[i]:
                if (j==t+19 or j==t-19 or j==t+1 or j==t-1) and x==0:
                    a=a+black[i]
                    h.append(i)
                    x=1
        black.append(a)
        for k in h:
            black.remove(other[k])
        return black   
    else:
        h=[]
        other=[]
        a=[t]
        for i in white:
            other.append(i)
        for i in range(0,len(white)):
            x=0
            for j in black[i]:
                if (j==t+19 or j==t-19 or j==t+1 or j==t-1) and x==0:
                    a=a+black[i]
                    h.append(i)
                    x=1
        white.append(a)
        for k in h:
            white.remove(other[k])
        return white  

def shuqi(i):
    q=0
    for v in dots:
        d=False
        for j in i:
            if v==j-1 or v==j+1 or v==j+19 or v==j-19:
                d=True
        if d:
            q=q+1
    return q

def tizi(t,steps):
    if steps%2==0:
        for i in white:
            e=False
            for j in i:
                if j==t-1 or j==t+1 or j==t+19 or j==t-19:
                    e=True
            if e:
                if shuqi(i)==0:
                    white.remove(i)
                    for w in i:
                        dots.append(w)
                        z=40+30*(w%19)
                        p=40+30*(w//19)
                        pygame.draw.circle(screen,[180,180,180],[int(z),int(p)],15,0)
                        pygame.draw.lines(screen,[0,0,0],False,[[int(z)-15,int(p)],[int(z)+15,int(p)]],1)
                        pygame.draw.lines(screen,[0,0,0],False,[[int(z),int(p)-15],[int(z),int(p)+15]],1)

    if steps%2==1:
        for i in black:
            e=False
            for j in i:
                if j==t-1 or j==t+1 or j==t+19 or j==t-19:
                    e=True
            if e:
                if shuqi(i)==0:
                    for w in i:
                        dots.append(w)
                        z=40+30*(w%19)
                        p=40+30*(w//19)
                        pygame.draw.circle(screen,[180,180,180],[int(z),int(p)],15,0)
                        pygame.draw.lines(screen,[0,0,0],False,[[int(z)-15,int(p)],[int(z)+15,int(p)]],1)
                        pygame.draw.lines(screen,[0,0,0],False,[[int(z),int(p)-15],[int(z),int(p)+15]],1)

def finddots(a,b):
    for k in adots:
        if a-12<=k[0]<=a+12 and b-12<=k[1]<=b+12:
            return k

def judge(a,b):
    for k in adots:
        if a-12<=k[0]<=a+12 and b-12<=k[1]<=b+12:
            return True        
    
    
                
for i in range(19):
    for j in range(19):
        dots.append(i+19*j)
        adots.append([40+30*i,40+30*j])


for i in range(19):
    pygame.draw.lines(screen,[0,0,0],False,[[40+30*i,40],[40+30*i,580]],1)
for j in range(19):
    pygame.draw.lines(screen,[0,0,0],False,[[40,40+30*j],[580,40+30*j]],1)
while running:
    r=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            a=event.pos[0]
            b=event.pos[1]
            t=finddots(a,b)
            r=judge(a,b)
            if r:
                n=(steps%2)*255
                pygame.draw.circle(screen,[n,n,n],t,15,0)
                g=(t[0]-40)/30+19*(t[1]-40)/30
                dots.remove(g)
                reaarange(g,steps)
                tizi(g,steps)
                steps=steps+1

    pygame.display.flip()     
pygame.quit()