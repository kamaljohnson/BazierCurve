import pygame
import random
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1300,800))
#colors
Black = (0,0,0)
White = (255,255,255)
Blue = (200,100,200)

Red = (255,0,50)
first4 = 0
screen.fill(Black)

listofpoints = []
mousepress = False
limit = 10000
flag = 0
flag1 = 0
lastpoint = (0,0)
fp = 0
list = []
size = 4
counter = 0
counter1 = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepress = True


    mpos = pygame.mouse.get_pos()
    if first4 == 1 and flag1 == 1:
        flag1 = 0
        a = list[-1]
        b = lastpoint
        c = (2*b[0]-a[0],2*b[1]-a[1])
        list = []
        list.append(c)
        pygame.draw.circle(screen, White, list[-1], 3, 3)
    if len(listofpoints) == 1 and first4 == 1 and mousepress == True:
        mousepress = False
        listofpoints.append(mpos)
        pygame.draw.circle(screen, White, mpos, 3, 3)
    if len(listofpoints) == 2 and first4 == 1 and mousepress == True:
        mousepress = False
        list.append(mpos)
        pygame.draw.circle(screen, White, mpos, 3, 3)
    if len(listofpoints) < 4 and mousepress == True and first4 != 1:
        listofpoints.append(mpos)
        pygame.draw.circle(screen,White,mpos,3,3)
        mousepress = False
    pygame.display.update()
    if (len(listofpoints)%4 == 0 or (len(listofpoints)%2 == 0 and first4 == 1 and len(list)%2 == 0))and flag == 0 and len(listofpoints) != 0:
        flag = 1
        flag1 = 1
        if first4 == 0:
            a = listofpoints[0]
            b = listofpoints[2]
            c = listofpoints[3]
            d = listofpoints[1]
            fp = listofpoints[1]
        else:
            a = listofpoints[0]
            b = list[0]
            c = list[1]
            d = listofpoints[1]
            fp = d

        lastpoint = d
        if first4 == 0:
            list.append(b)
            list.append(c)
        first4 = 1
        for l in range(limit):
            m = limit - l
            a1 = ((m*a[0] + b[0])/(m+1),(m*a[1] + b[1])/(m+1))
            b1 = ((m*b[0] + c[0])/(m+1),(m*b[1] + c[1])/(m+1))
            c1 = ((m*c[0] + d[0])/(m+1),(m*c[1] + d[1])/(m+1))
            pygame.draw.line(screen, Red, a, a1, size)
            #if m%(int(limit/10)) == 0:
            pygame.draw.line(screen,Blue, a, b, 1)
            pygame.draw.line(screen,Blue, b, c, 1)
            pygame.draw.line(screen,Blue, c, d, 1)
            a = a1
            b = b1
            c = c1
            pygame.display.update()
        pygame.draw.line(screen, Red, a1, d, size)
        listofpoints = []
        listofpoints.append(fp)
        flag = 0
    pygame.display.update()