import pygame
from pygame.locals import *
pygame.init()


class LoadImage:
    def __init__(self, img_path):
        self.img_path = img_path

    def show_image(self, xy, scr):
        scr.blit(pygame.image.load(self.img_path), xy)

    def show_transform_image(self, xy, width, height, scr):
        scr.blit(pygame.transform.smoothscale(pygame.image.load(self.img_path), (width, height)), xy)
