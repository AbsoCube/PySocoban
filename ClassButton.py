import pygame
import sys
import random
from pygame.locals import *
'''
Button3.0 by AbsoCube Studio
Button3.0 Update Log:
Update Time : 2020/2/21 Friday
Update Contents :
    Remove redundant functions and add color_update.
'''

class button():
    def __init__(self, posx, posy, length, width, text, bfont, color, textcolor=(0, 0, 0)):
        self.posx = posx
        self.posy = posy
        self.color = color
        self.length = length
        self.width = width
        self.tcolor = textcolor
        self.font = bfont
        self.text = text
        if self.tcolor == "opposite":
            tcl = []
            for c in color:
                tcl.append(255-c)
            self.textcolor = (tcl[0], tcl[1], tcl[2])
        else:
            self.textcolor = textcolor
        self.rect = pygame.Rect(self.posx, self.posy, length, width)

    def show(self, scr):
        if self.color:
            scr.fill(self.color, self.rect)
        text = self.font.render(self.text, True, self.textcolor)
        text_rect = text.get_rect()
        text_rect.centerx = self.posx+self.length//2
        text_rect.centery = self.posy+self.width//2
        scr.blit(text, text_rect)

    def pressed(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if button == 1 or 3:
                mousedownx, mousedowny = event.pos
                if self.posx <= mousedownx <= self.posx+self.length and self.posy <= mousedowny <= self.posy+self.width:
                    return True
                else:
                    return False

    def color_update(self):
        if self.tcolor == "opposite":
            tcl = []
            for c in self.color:
                tcl.append(255-c)
            self.textcolor = (tcl[0], tcl[1], tcl[2])


if __name__ == "__main__":
    buttonlength = int(input("set button's length:"))
    buttonwidth = int(input("set button's width:"))
    fontsize = int(input("set font's size:"))
    pygame.init()
    screen = pygame.display.set_mode((buttonlength + 40, buttonwidth + 40))
    pygame.display.set_caption("Class Button Example")
    pfont = pygame.font.Font("font/Mouse.ttf", fontsize)
    change = button(20, 20, buttonlength, buttonwidth, "change", pfont, (255, 255, 255), "opposite")
    print("\npress button 'change' to change its color.")
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if change.pressed(event):
                randomcolor = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
                change.color = randomcolor
                change.color_update()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        change.show(screen)
        pygame.display.update()
