import pygame as pg


def edit_size_menu(win_size, img):
    return pg.transform.scale(img, (int(win_size[0] * 1.3 + 1), int(win_size[-1] * 1.3)))
