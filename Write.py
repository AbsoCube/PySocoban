import pygame
pygame.init()


class Write:
    def __init__(self, text, color, scr):
        self.text = text
        self.color = color
        self.scr = scr
        self.sRect = self.scr.get_rect()

    def show_center(self):
        mcfont = pygame.font.Font("font/Mouse.ttf", 50)
        write = mcfont.render(self.text, True, self.color)
        wrect = write.get_rect()
        wrect.centerx = self.sRect.centerx
        wrect.centery = self.sRect.centery
        self.scr.blit(write, wrect)
