# -*- coding:utf-8 -*-
import pygame, sys, time, random
from ClassButton import button
from Write import Write
from ShowImage import ShowImage
from pygame.locals import *
pygame.init()
# create
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Sokaban")
pygame.display.set_icon(pygame.image.load("images/icon.ico"))
screen.fill((255, 255, 255))
# load imgaes
Steve = ShowImage("images/Steve.png")
Alex = ShowImage("images/Alex.png")
plank = ShowImage("images/plank.png")
case = ShowImage("images/case.png")
TPH = ShowImage("images/TPH.png")
bg = ShowImage("images/grassfarm.jpg")
# get font
mcfont = pygame.font.Font("font/Mouse.ttf", 50)
text1 = Write("Easy\tNormal\tHard\tRandom", (0, 0, 0), screen)
choose_text = mcfont.render("Choose difficulty:", True, (0, 0, 0))
ctrect = choose_text.get_rect()
ctrect.centerx = 400
ctrect.centery = 325
# new button
pfont = pygame.font.Font("font/Mouse.ttf", 30)
play = button(350, 450, 100, 50, "Play", pfont, (71, 1, 3), textcolor = (255, 255, 255))
# Game conditions
starts = False
chooses = True
easy = False
normal = False
hard = False
randoms = False
plays = False
# 'pc' point
use_time = time.time()
# MaxScore
file = open("MaxScore.s", "w")
# show logo
TPH.show_transform_image((250, 275), 300, 250, screen)
pygame.display.update()
time.sleep(3)
# games
while True:
    """get mouse pos and game keys!"""
    mx, my = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            etime = time.time() - use_time
            etime = "%.2f" % eitme
            file.write(etime)
            file.close()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if not starts:
                    if chooses:
                        if 73 <= mx <= 186 and 375 <= my <= 425:
                            easy = True
                            normal = False
                            hard = False
                            randoms = False
                            plays = True
                        if 210 <= mx <= 375 and 375 <= my <= 425:
                            easy = False
                            normal = True
                            hard = False
                            randoms = False
                            plays = True
                        if 398 <= mx <= 513 and 375 <= 425:
                            easy = False
                            normal = False
                            hard = True
                            randoms = False
                            plays = True
                        if 535 <= mx <= 723 and 375 <= 425:
                            easy = False
                            normal = False
                            hard = False
                            randoms = True
                            plays = True
    # game not start
    if not starts:
        bg.show_image((0, 0), screen)
        if chooses:
            text1.show_center()
            screen.blit(choose_text, ctrect)
            if easy or normal or hard or randoms:
                if plays:
                    play.show(screen)
                    if play.pressed(event):
                        starts = True
    # game start
    elif starts:
        bg.show_image((0, 0), screen)
        plank.show_image((0, 0), screen)
    # update game
    pygame.display.update()
