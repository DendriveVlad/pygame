import pygame as pg

import SizeMenager as Size

def settings(win):
    r = 1
    while r:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                r = 0

        win_size = win.get_size()

        pg.draw.rect(win, pg.Color("Black"),
                     (win_size[0] // 8, win_size[-1] // 8, win_size[0] // 2, win_size[-1] // 1.2)
                     )
        pg.draw.rect(win, pg.Color("White"),
                     (win_size[0] // 8, win_size[-1] // 8, win_size[0] // 2, win_size[-1] // 1.2)
                     , 2)
        text = pg.font.Font('JetBrains Mono Regular.ttf', 25)
        win.blit(text.render("Здесь пока что ничего нет :(", 255, (255, 255, 255)), (180, 100))

        pg.display.flip()
