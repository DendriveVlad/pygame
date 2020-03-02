import pygame as pg


def you_sure(win, win_size, play):
    r = 1
    while r:
        choise = [False, False]
        click = False
        pg.time.delay(10)

        mx, my = pg.mouse.get_pos()

        pg.draw.rect(win, pg.Color("Black"),
                     ((win_size[0] // 2 - 200, win_size[-1] // 2 - 60), (400, 120)))
        pg.draw.rect(win, pg.Color("White"),
                     ((win_size[0] // 2 - 200, win_size[-1] // 2 - 60), (400, 120)), 2)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                r = 0
            if event.type == pg.MOUSEBUTTONDOWN:
                click = True

        if win_size[0] // 2 - 198 < mx < win_size[0] // 2 and \
                win_size[-1] // 2 - 58 < my < win_size[-1] // 2 + 59:
            choise[0] = True
            pg.draw.rect(win, (207, 51, 51),
                         ((win_size[0] // 2 - 198, win_size[-1] // 2 - 58), (198, 117)))
        elif win_size[0] // 2 - 2 < mx < win_size[0] // 2 + 199 and \
                win_size[-1] // 2 - 58 < my < win_size[-1] // 2 + 59:
            choise[-1] = True
            pg.draw.rect(win, (11, 110, 92),
                         ((win_size[0] // 2, win_size[-1] // 2 - 58), (199, 117)))

        text = pg.font.Font('JetBrains Mono Regular.ttf', 30)
        win.blit(text.render("Выход", 255, (7, 218, 180)),
                 (win_size[0] // 2 - 150, win_size[-1] // 2 - 15))
        win.blit(text.render("Отмена", 255, (7, 218, 180)),
                 (win_size[0] // 2 + 50, win_size[-1] // 2 - 15))

        if click:
            if choise[0] and not play:
                exit()
            elif choise[0] and play:
                return False
            elif choise[-1]:
                r = 0

        pg.display.flip()

# Готово
