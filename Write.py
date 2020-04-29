import pygame
from pygame.locals import *
pygame.init()
class Write():
    def __init__(self, text, color, scr):
        self.text = text
        self.color = color
        self.scr = scr
    def show_center(self):
        mcfont = pygame.font.Font("font/Mouse.ttf", 50)
        write = mcfont.render(self.text, True, self.color)
        wrect = write.get_rect()
        wrect.centerx = 400
        wrect.centery = 400
        self.scr.blit(write, wrect)
