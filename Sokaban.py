# -*- coding:utf-8 -*-
import pygame, sys, time, random
from ClassButton import button
from Write import Write
from ShowImage import LoadImage
from pygame.locals import *
import numpy as np
from Maps import *
pygame.init()
# 游戏初始化
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PySocoban")
pygame.display.set_icon(pygame.image.load("images/icon.ico"))
# 加载资源
Steve = LoadImage("images/Steve.png")
plank = LoadImage("images/plank.png")
case = LoadImage("images/case.png")
TPH = LoadImage("images/TPH.png")
bg = LoadImage("images/grassfarm.jpg")
# 字体
mcfont = pygame.font.Font("font/Mouse.ttf", 50)
text1 = Write("Easy\tNormal\tHard\tRandom", (0, 0, 0), screen)
choose_text = mcfont.render("Choose difficulty:", True, (0, 0, 0))
ctrect = choose_text.get_rect()
ctrect.centerx = 400
ctrect.centery = 325
# 按钮
pfont = pygame.font.Font("font/Mouse.ttf", 30)
play = button(350, 450, 100, 50, "Play", pfont, (71, 1, 3), textcolor=(255, 255, 255))
# flags
starts = False
chooses = True
mode = ""
# MaxScore
file = open("MaxScore.s", "w")
# show logo
screen.fill((255, 255, 255))
TPH.show_transform_image((250, 275), 300, 250, screen)
pygame.display.update()
time.sleep(3)

# 游戏主循环
while True:
    # 按键检测
    mx, my = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and not starts and chooses:
                if 73 <= mx <= 186 and 375 <= my <= 425:
                    mode = "easy"
                if 210 <= mx <= 375 <= my <= 425:
                    mode = "normal"
                if 398 <= mx <= 513 and 375 <= my <= 425:
                    mode = "hard"
                if 535 <= mx <= 723 and 375 <= my <= 425:
                    mode = "random"
        if play.pressed(event) and mode:
            starts = True
            gmap = maps[mode]

    # 游戏封面
    if not starts:
        bg.show_image((0, 0), screen)
        play.show(screen)
        if chooses:
            text1.show_center()
            screen.blit(choose_text, ctrect)

    # 游戏
    elif starts:
        bg.show_image((0, 0), screen)
        for index1 in range(0, 16):
            for index2 in range(0, 16):
                if gmap[index1][index2] == 1:
                    plank.show_image((index1*50, index2*50), screen)
                elif gmap[index1][index2] == 2:
                    case.show_image((index1*50, index2*50), screen)
                elif gmap[index1][index2] == 3:
                    Steve.show_image((index1*50, index2*50), screen)

    pygame.display.update()
