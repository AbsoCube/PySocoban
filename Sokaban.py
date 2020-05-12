# -*- coding:utf-8 -*-
import pygame, sys, time, random
from ClassButton import button
from Write import Write
from ShowImage import LoadImage
from pygame.locals import *
from Maps import *
pygame.init()
# 游戏初始化
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("PySocoban")
pygame.display.set_icon(pygame.image.load("images/PyCase.ico"))
# 加载资源
Steve = LoadImage("images/Steve.png")
plank = LoadImage("images/plank.png")
case = LoadImage("images/case.png")
TPH = LoadImage("images/TPH.png")
bg = LoadImage("images/grassfarm.jpg")
sign = LoadImage("images/sign.png")
back = LoadImage("images/back.png")
finish = LoadImage("images/finish.png")
# 字体
mcfont = pygame.font.Font("font/Mouse.ttf", 50)
text1 = Write("Easy\tNormal\tHard\tRandom", (0, 0, 0), screen)
choose_text = mcfont.render("Choose difficulty:", True, (0, 0, 0))
back_text = mcfont.render("back", True, (0, 0, 0))
ctrect = choose_text.get_rect()
ctrect.centerx = 400
ctrect.centery = 325
# point
up_point = time.time()
down_point = time.time()
# 按钮
pfont = pygame.font.Font("font/Mouse.ttf", 30)
play = button(350, 450, 100, 50, "Play", pfont, (71, 1, 3), textcolor=(255, 255, 255))
# flags
starts = False
chooses = True
mode = ""
# 坐标偏移
rel_x = 0
rel_y = 0
move = "no"
# show logo
screen.fill((255, 255, 255))
TPH.show_transform_image((250, 275), 300, 250, screen)
pygame.display.update()
time.sleep(3)
# BGM
bgm_time = time.time()
pygame.mixer.music.stop()
pygame.mixer.music.load("music/C418 - Minecraft.mp3")
pygame.mixer.music.play()


def replace(pos1, respos):
    global gmap
    target = (pos1[0] + respos[0], pos1[1] + respos[1])
    if gmap[target[0]][target[1]] != 0 and gmap[target[0]][target[1]] != 2:
        return False
    elif gmap[target[0]][target[1]] == 0:
        gmap[target[0]][target[1]] = gmap[pos1[0]][pos1[1]]
        gmap[pos1[0]][pos1[1]] = 0
        return True
    elif gmap[target[0]][target[1]] == 2:
        if gmap[target[0] + respos[0]][target[1] + respos[1]] == 0 or \
                gmap[target[0] + respos[0]][target[1] + respos[1]] == 4:
            if gmap[target[0] + respos[0]][target[1] + respos[1]] == 4:
                gmap[target[0] + respos[0]][target[1] + respos[1]] = 5
            else:
                gmap[target[0] + respos[0]][target[1] + respos[1]] = gmap[target[0]][target[1]]
            gmap[target[0]][target[1]] = gmap[pos1[0]][pos1[1]]
            gmap[pos1[0]][pos1[1]] = 0
            return True
        else:
            return False


# 游戏主循环
while True:
    # 音乐循环播放
    if time.time() - bgm_time >= 254:
        pygame.mixer.music.stop()
        pygame.mixer.music.load("music/C418 - Minecraft.mp3")
        pygame.mixer.music.play()
        bgm_time = time.time()
    # 按键检测
    mx, my = pygame.mouse.get_pos()
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
                if 10 <= mx <= 40 and 15 <= my <= 35:
                    if starts:
                        starts = False
        if play.pressed(event) and mode:
            starts = True
            gmap = maps[mode]

            # Steve坐标
            for index1 in range(0, 16):
                for index2 in range(0, 16):
                    if gmap[index1][index2] == 3:
                        StevePos = (index1, index2)

    keys = pygame.key.get_pressed()
    if starts and move == "no":
        if keys[K_DOWN]:
            move = "down"
        elif keys[K_UP]:
            move = "up"
        elif keys[K_LEFT]:
            move = "left"
        elif keys[K_RIGHT]:
            move = "right"

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

        # 移动
        if move == "up":
            rel_y -= 0.2
        elif move == "down":
            rel_y += 0.2
        elif move == "left":
            rel_x -= 0.2
        elif move == "right":
            rel_x += 0.2

        # 检查移动是否结束
        if abs(rel_x) >= 1 or abs(rel_y) >= 1:
            move = "no"
            if replace((StevePos[0], StevePos[1]), (int(rel_x), int(rel_y))):
                StevePos = (int(StevePos[0] + rel_x), int(StevePos[1] + rel_y))
            rel_x = 0
            rel_y = 0

        for index1 in range(0, 16):
            for index2 in range(0, 16):
                if gmap[index1][index2] == 1:
                    plank.show_image((index1 * 50, index2 * 50), screen)
                elif gmap[index1][index2] == 2:
                    case.show_image((index1 * 50, index2 * 50), screen)
                elif gmap[index1][index2] == 3:
                    Steve.show_transform_image(((index1 + rel_x) * 50, (index2 + rel_y) * 50), 50, 50, screen)
                elif gmap[index1][index2] == 4:
                    sign.show_transform_image((index1 * 50, index2 * 50), 50, 50, screen)
                elif gmap[index1][index2] == 5:
                    finish.show_transform_image((index1 * 50, index2 * 50), 50, 50, screen)
        back.show_transform_image((10, 15), 30, 20, screen)
        screen.blit(back_text, (50, 5))

    pygame.display.update()
