import pygame as pg  # pygame :/
from pygame.locals import *  # Особые константы для монипуляции PyGame'ом
import ctypes  # Для работы с монитором
from random import randint as rint

import DevConsole as Cmd  # Консоль разработчика
import MainMenu as Menu  # Главное меню
import SizeMenager as Size  # Изменение размеров
import ExitWindow as Exit  # Обработка выхода из игры
import Game  # Сама игра

pg.init()  # Инициализцая PyGame

user32 = ctypes.windll.user32
USER_MONITOR = user32.GetSystemMetrics(0), user32.GetSystemMetrics(
    1)  # Получает разрешение монитора пользователя
FULLSCREEN_GAME = 0  # Открыта ли игра в полный экран
GAME_SIZE = (1280, 720)  # Размер стартового окна
isPlaying = False  # Запущена ли сама игра(True) или игрок находится в главном меню(False)
click = False  # Проверка нажатий
clock = pg.time.Clock()

pg.display.set_caption("Бестолочь THE GAME")  # Название окна
win = pg.display.set_mode(GAME_SIZE)  # Открывается окно игры с разрешением 720p
pg.display.set_icon(pg.image.load("ico.ico"))  # Ставит иконку

GAME_MENU = Menu.Menu(win, GAME_SIZE)
GAME_MENU.background = Size.edit_size_menu(GAME_SIZE, GAME_MENU.background)

NPC = Game.Entity(win, GAME_SIZE)
PLAYER = Game.Player(win, GAME_SIZE, NPC)

frame = 0
r = 1  # Переменная работы программы. Если она == 0, то программа выключается
while r:
    clock.tick(60)  # игра в 60 fps
    frame += 1 if frame != 59 else -59
    # Проверка запущена ли игра или игрок находится в меню
    if isPlaying:
        NPC.entity_draw()
        PLAYER.player_move(frame)
        if rint(0, 100) == 100:
            NPC.spawn_entity((rint(10, GAME_SIZE[0] - 60), rint(10, GAME_SIZE[-1] - 60)))
    else:
        isPlaying = GAME_MENU.background_menu(click)  # Ставит задний фон меню
    click = False

    for event in pg.event.get():  # Проверка на какое-либо действе со стороны пользователя
        if event.type == pg.QUIT:  # Проверка на нажатие выхода (крестик)
            r = 0
        if event.type == KEYDOWN and event.key == K_BACKQUOTE:
            Cmd.copen(win, GAME_SIZE, isPlaying, PLAYER, NPC)  # Открывает консоль
        if event.type == MOUSEBUTTONDOWN:
            if isPlaying:
                PLAYER.player_attack()
            else:
                click = True
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            a = isPlaying
            isPlaying = Exit.you_sure(win, GAME_SIZE, isPlaying)
            if a:
                NPC = Game.Entity(win, GAME_SIZE)
                PLAYER = Game.Player(win, GAME_SIZE, NPC)

    key_pressed = pg.key.get_pressed()  # Список со всеми возможными кнопками, которые можно нажать
    if key_pressed[K_F11]:  # Вывод игры на полный экран или в оконный режим при нажатии F11
        if FULLSCREEN_GAME:
            FULLSCREEN_GAME = 0
            GAME_SIZE = (1280, 720)  # Открывается окно игры с разрешением 720p
            win = pg.display.set_mode(GAME_SIZE)
        else:
            FULLSCREEN_GAME = 1
            GAME_SIZE = USER_MONITOR
            win = pg.display.set_mode(USER_MONITOR, pg.FULLSCREEN)  # Делает игру на полный экран

        GAME_MENU.background = Size.edit_size_menu(GAME_SIZE, GAME_MENU.background)

        GAME_MENU.win_size = GAME_SIZE
        PLAYER.win_size = GAME_SIZE
    a = False

    pg.display.flip()  # Выводит все изменения на экран
