import pygame as pg

import ExitWindow as Exit
import SettingsWindow as Settings

pg.init()


class Menu:
    def __init__(self, win, win_size):
        self.win = win
        self.win_size = win_size
        self.background = pg.image.load("background.jpg!d").convert().convert_alpha()

    def background_menu(self, click):
        self.win.fill((0, 0, 0))
        mousex, mousey = pg.mouse.get_pos()
        x = (self.win_size[0] // 2 - mousex - mousex // 3.33 * 1000) // 1000
        y = (self.win_size[-1] // 2 - mousey - mousey // 3.33 * 1000) // 1000
        self.win.blit(self.background, (x, y))
        return self.menu_buttons(mousex, mousey, click)

    def menu_buttons(self, mousex, mousey, click):
        button_pos = self.win_size[0] - 300, self.win_size[-1] // 2

        button_color = (70, 74, 84)
        aim_color = (11, 110, 92)
        exit_color = (207, 51, 51)

        text_color = (7, 218, 180)

        bContineu = [(button_pos[0], button_pos[-1] - 125, 180, 50), False]
        bPlay = [(button_pos[0], button_pos[-1] - 75, 180, 50), False]
        bSettings = [(button_pos[0], button_pos[-1] - 25, 180, 50), False]
        bNoInGame = [(button_pos[0], button_pos[-1] + 25, 180, 50), False]
        bExit = [(button_pos[0], button_pos[-1] + 75, 180, 50), False]

        if bContineu[0][0] <= mousex <= bContineu[0][0] + bContineu[0][-2] and \
                bContineu[0][1] <= mousey <= bContineu[0][1] + bContineu[0][-1]:
            bContineu[-1] = True
        elif bPlay[0][0] <= mousex <= bPlay[0][0] + bPlay[0][-2] and \
                bPlay[0][1] <= mousey <= bPlay[0][1] + bPlay[0][-1]:
            bPlay[-1] = True
        elif bSettings[0][0] <= mousex <= bSettings[0][0] + bSettings[0][-2] and \
                bSettings[0][1] <= mousey <= bSettings[0][1] + bSettings[0][-1]:
            bSettings[-1] = True
        elif bNoInGame[0][0] <= mousex <= bNoInGame[0][0] + bNoInGame[0][-2] and \
                bNoInGame[0][1] <= mousey <= bNoInGame[0][1] + bNoInGame[0][-1]:
            bNoInGame[-1] = True
        elif bExit[0][0] <= mousex <= bExit[0][0] + bExit[0][-2] and \
                bExit[0][1] <= mousey <= bExit[0][1] + bExit[0][-1]:
            bExit[-1] = True

        text = pg.font.Font('JetBrains Mono Regular.ttf', 25)
        textNoInGame = pg.font.Font('JetBrains Mono Regular.ttf', 15)

        play = [
            # button_color if not bContineu[-1] else aim_color
            [pg.draw.rect(self.win, (207, 150, 51), bContineu[0]),
             self.win.blit(text.render("Продолжить", 255, text_color),
                           (bContineu[0][0] + 15, bContineu[0][1] + 10))],

            [pg.draw.rect(self.win, button_color if not bPlay[-1] else aim_color, bPlay[0]),
             self.win.blit(text.render("Играть", 255, text_color),
                           (bPlay[0][0] + 43, bPlay[0][1] + 10))],
            [pg.draw.rect(self.win, button_color if not bSettings[-1] else aim_color, bSettings[0]),
             self.win.blit(text.render("Настройки", 255, text_color),
                           (bSettings[0][0] + 22, bSettings[0][1] + 10))],
            # button_color if not bNoInGame[-1] else aim_color
            [pg.draw.rect(self.win, (207, 150, 51), bNoInGame[0]),
             self.win.blit(textNoInGame.render("Режим разработчика", 255, text_color),
                           (bNoInGame[0][0] + 10, bNoInGame[0][1] + 15))],

            [pg.draw.rect(self.win, button_color if not bExit[-1] else exit_color, bExit[0]),
             self.win.blit(text.render("Выход", 255, text_color),
                           (bExit[0][0] + 50, bExit[0][1] + 10))]
        ]

        if click:
            if bContineu[-1]:
                pass
            if bPlay[-1]:
                return True
            if bSettings[-1]:
                Settings.settings(self.win)
            if bNoInGame[-1]:
                pass
            if bExit[-1]:
                Exit.you_sure(self.win, self.win_size, False)

        return False
