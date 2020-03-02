import pygame as pg

import Game

pg.init()

LOGS = ["Введите \"help\", чтобы увидет список команд"]


def copen(win, win_size, isPlaying, player, npc):
    console_win = Console(win, win_size, isPlaying, player, npc)
    console_win.draw_console_win()

    pg.display.flip()
    pg.time.delay(300)
    console_input(win, win_size, console_win)


def console_input(win, win_size, console_win):
    text = ""
    r = 1
    while r:
        pg.time.delay(10)
        for event in pg.event.get():
            inputing = pg.font.Font('JetBrains Mono Regular.ttf', 25)
            logs = pg.font.SysFont('arial', 15)
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN and (event.key == pg.K_BACKQUOTE or event.key == pg.K_ESCAPE):
                r = 0
                text = ""
                break
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if text == "":
                        pass
                    else:
                        console_win.splitter(text)
                    text = ""

                elif event.key == pg.K_BACKSPACE and len(text) > 0:
                    text = text[:-1]
                else:
                    if len(text) == 42:
                        pass
                    else:
                        if (text == "" or text[
                            -1] == " ") and event.unicode == " " or event.key == pg.K_TAB or \
                                event.key == pg.K_BACKSPACE or event.key == pg.K_KP_ENTER or \
                                event.key == pg.K_LCTRL or event.type == event.key == pg.K_RCTRL:
                            pass
                        elif event.key == pg.K_F11:
                            LOGS.append(
                                "Нельзя выйти или войти в полноэкранный режим, когда вы находитесь"
                                "в консоли")
                        else:
                            text += event.unicode
            console_win.draw_console_win()
            win.blit(inputing.render(text, 0, (255, 255, 255)), (5, win_size[-1] // 2 - 38))
            mess_pos = win_size[-1] // 2 - 60
            for log_number in range(1, len(LOGS) + 1):
                win.blit(logs.render(LOGS[-log_number], 0, (255, 255, 255)), (5, mess_pos))
                mess_pos -= 15
        if len(LOGS) > 50:
            del LOGS[0]

        pg.display.flip()


class Console:
    def __init__(self, win, win_size, isPlaying, player, npc):
        self.win = win
        self.win_size = win_size
        self.Play = isPlaying
        self.player = player
        self.npc = npc

    def draw_console_win(self):
        pg.draw.rect(self.win, pg.Color("Black"),
                     ((0, 0), (self.win_size[0] // 2, self.win_size[-1] // 2)))
        pg.draw.rect(self.win, pg.Color("White"),
                     ((0, 0), (self.win_size[0] // 2, self.win_size[-1] // 2)), 2)
        pg.draw.line(self.win, pg.Color("White"), (0, self.win_size[-1] // 2 - 40),
                     (self.win_size[0] // 2, self.win_size[-1] // 2 - 40), 2)

    def splitter(self, message):
        command = message.split()[0].lower()
        try:
            attribute = message.split()[1].lower()
        except IndexError:
            attribute = ""

        if command == "help":
            self.help_concole()
        elif command == "print":
            self.print_mess_in_console(attribute)
        elif command == "hitbox":
            self.hitbox(attribute)
        elif command == "click_wnpc_spawn" and self.Play:
            self.click_wnpc_spawn(attribute)
        else:
            self.error()

    def error(self):
        LOGS.append("Неверная команда")

    def help_concole(self):
        LOGS.append("")
        LOGS.append("-----------------Все консольные команды------------------------")
        LOGS.append("print <Сообщение> - Отправляет \"Сообщение\" в консоль")
        LOGS.append("hitbox on/off - Включает или выключает хитбоксы")
        LOGS.append("click_wnpc_spawn <Кол-во спавнов> - Заспавнить моба в месте клика")
        LOGS.append("----------------------------------------------------------------------------")
        LOGS.append("")

    def print_mess_in_console(self, message):
        LOGS.append(message)

    def hitbox(self, option):
        if option == "on":
            LOGS.append("Хитбоксы включены")

        elif option == "off":
            LOGS.append("Хитбоксы отключены")
        else:
            LOGS.append("Неверно введён атрибут для команды")
            LOGS.append("hitbox on/off")

    def click_wnpc_spawn(self, count):
        try:
            count = int(count)
        except ValueError:
            LOGS.append("Неверное значение атрибута")
            LOGS.append("click_wnpc_spawn <Кол-во спавнов(число)>")
            return

        if count < 1:
            LOGS.append("Неверное значение атрибута")
            LOGS.append("click_wnpc_spawn <Кол-во спавнов(Больше 0)>")
        else:
            for i in range(count):
                while 1:
                    stop = False
                    for event in pg.event.get():
                        if event.type == pg.MOUSEBUTTONDOWN:
                            mx, my = pg.mouse.get_pos()
                            self.npc.spawn_entity((mx - 25, my - 25))
                            stop = True
                    self.win.fill((0, 0, 0))
                    self.player.draw_player()
                    self.npc.entity_draw()
                    pg.display.flip()
                    if stop:
                        break

                LOGS.append("Моб заспавнен")
