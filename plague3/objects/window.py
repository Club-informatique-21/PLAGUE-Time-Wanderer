#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""DAT FILE WINDOW"""
import pygame


class Window(object):
    """DAT CLASS WINDOW"""
    def __init__(self, /, icon: str, title: str, subtitle, width: int = 500, height: int = 500):
        self.icon: str = icon
        self.title: str = title
        self.subtitle: str = subtitle
        self.width: int = width
        self.height: int = height
        self.surface: pygame.Surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title, self.subtitle)
        pygame.display.set_icon(pygame.image.load(self.icon))

    def add_image(self):
        return None

    @staticmethod
    def calccenter(img):
        scsize = (self.width, self.height)
        isl = img.get().get_size()
        return round(scsize[0] / 2 - isl[0] / 2), round(scsize[1] / 2 - isl[1] / 2)