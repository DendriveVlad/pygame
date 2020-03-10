import pygame as pg
from pygame.locals import *


class Player:
    def __init__(self, win, win_size, entity):
        self.frame = 0
        self.anim = Animation(win)
        self.win = win
        self.win_size = win_size
        self.player_position = [self.win_size[0] // 2 - 25, self.win_size[-1] // 2 - 25]
        self.player_collision = (50, 50)
        self.player_aim = pg.draw.circle(self.win, (255, 255, 255), pg.mouse.get_pos(), 3, 1)
        self.player_speed = 5
        self.bullets = []
        self.entity = entity
        self.isMoving = False
        self.isPunch = False
        self.punch = (0, 0)

        self.one_second = 0

    def player_move(self, frame):
        self.frame = frame
        key_pressed = pg.key.get_pressed()
        self.isMoving = False

        if key_pressed[K_LSHIFT]:
            self.player_speed = 7
            self.isMoving = True

        if key_pressed[K_w]:
            self.player_position[-1] -= self.player_speed
            self.isMoving = True

        if key_pressed[K_a]:
            self.player_position[0] -= self.player_speed
            self.isMoving = True

        if key_pressed[K_s]:
            self.player_position[-1] += self.player_speed
            self.isMoving = True

        if key_pressed[K_d]:
            self.player_position[0] += self.player_speed
            self.isMoving = True

        self.player_speed = 5
        self.draw_player()

    def player_attack(self):
        mx, my = pg.mouse.get_pos()
        damage_pos = 0
        # right = pg.draw.polygon(self.win, (255, 255, 255),
        #                         ((self.player_position[0] + 25, self.player_position[-1] + 25),
        #                          (self.player_position[0] + 5025, self.player_position[-1] + 5025),
        #                          (self.player_position[0] + 5025, self.player_position[-1] - 5025)))
        # down = pg.draw.polygon(self.win, (255, 255, 0),
        #                        ((self.player_position[0] + 25, self.player_position[-1] + 25),
        #                         (self.player_position[0] + 5025, self.player_position[-1] + 5025),
        #                         (self.player_position[0] - 5025, self.player_position[-1] + 5025)))
        # left = pg.draw.polygon(self.win, (255, 0, 255),
        #                        ((self.player_position[0] + 25, self.player_position[-1] + 25),
        #                         (self.player_position[0] - 5025, self.player_position[-1] + 5025),
        #                         (self.player_position[0] - 5025, self.player_position[-1] - 5025)))
        # up = pg.draw.polygon(self.win, (0, 255, 255),
        #                      ((self.player_position[0] + 25, self.player_position[-1] + 25),
        #                       (self.player_position[0] - 5025, self.player_position[-1] - 5025),
        #                       (self.player_position[0] + 5025, self.player_position[-1] - 5025)))

        damage_pos = (self.player_position[0] + 60, self.player_position[-1] - 10,
                      self.player_position[0] + 80, self.player_position[-1] + 60)

        # if self.win.get_at((mx, my))[0:3] == (255, 255, 255):  # right
        #     damage_pos = (self.player_position[0] + 60, self.player_position[-1] - 10,
        #                   self.player_position[0] + 80, self.player_position[-1] + 60)
        # elif self.win.get_at((mx, my))[0:3] == (255, 0, 255):  # left
        #     damage_pos = (self.player_position[0] - 30, self.player_position[-1] - 10,
        #                   self.player_position[0] - 10, self.player_position[-1] + 60)
        #     self.win.fill((0, 0, 0))
        #     pg.draw.rect(self.win, (255, 255, 255), (damage_pos[0], damage_pos[1], 20, 70))
        # elif self.win.get_at((mx, my))[0:3] == (255, 255, 0):  # down
        #     damage_pos = (self.player_position[0] - 10, self.player_position[-1] + 60,
        #                   self.player_position[0] + 60, self.player_position[-1] + 80)
        #     self.win.fill((0, 0, 0))
        #     pg.draw.rect(self.win, (255, 255, 255), (damage_pos[0], damage_pos[1], 70, 20))
        # elif self.win.get_at((mx, my))[0:3] == (0, 255, 255):  # up
        #     damage_pos = (self.player_position[0] - 10, self.player_position[-1] - 30,
        #                   self.player_position[0] + 60, self.player_position[-1] - 10)
        #     self.win.fill((0, 0, 0))
        #     pg.draw.rect(self.win, (255, 255, 255), (damage_pos[0], damage_pos[1], 70, 20))
        self.entity.entity_draw()
        self.draw_player()

        self.isPunch = True
        self.punch = damage_pos[0:2]

        self.entity.entity_damage(24, damage_pos)

    def draw_player(self):
        if self.isPunch:
            self.isPunch = self.anim.attack(self.punch, self.frame)
        if self.isMoving:
            self.anim.move(self.player_position, self.frame)
        else:
            self.anim.stop(self.player_position)
        self.player_aim = pg.draw.circle(self.win, (255, 255, 255), pg.mouse.get_pos(), 10, 1)


class Entity:
    def __init__(self, win, win_size):
        self.win = win
        self.win_size = win_size
        self.entities = []
        self.baground = pg.image.load("bg.png").convert().convert_alpha()

    def spawn_entity(self, spawn_position):
        self.entities.append(
            ["pg.draw.rect(self.win, (169, 49, 14), (" + str(spawn_position) + ", (50, 50)))",
             list(spawn_position), (50, 50), 100])

    def entity_damage(self, damage, damage_pos):
        for entity in self.entities:
            pox = False
            for ex in range(entity[1][0], entity[1][0] + 50):
                leave = 0
                for dx in range(damage_pos[0], damage_pos[2]):
                    if ex == dx:
                        print(damage_pos, ex, dx)
                        pox = True
                        leave = 1
                        break
                if leave:
                    break
            if pox:
                for ey in range(entity[1][1], entity[1][1] + 50):
                    leave = 0
                    for dy in range(damage_pos[1], damage_pos[-1]):
                        if ey == dy:
                            self.entities[self.entities.index(entity)][-1] -= damage
                            print(damage_pos, ey, dy)
                            leave = 1
                            break
                    if leave:
                        break
            if self.entities[self.entities.index(entity)][-1] < 1:
                del self.entities[self.entities.index(entity)]

    def entity_draw(self):
        self.win.fill((0, 0, 0))
        self.win.blit(self.baground, (0, 0))
        for i in self.entities:
            exec(i[0])


class Animation:
    def __init__(self, win):
        self.win = win

        self.walk = [pg.image.load("walk/1.png").convert_alpha(),
                     pg.image.load("walk/2.png").convert_alpha()]
        self.stay = pg.image.load("stay.png").convert_alpha()
        self.punch = [pg.image.load("punch/1.png").convert_alpha(),
                      pg.image.load("punch/2.png").convert_alpha(),
                      pg.image.load("punch/3.png").convert_alpha(),
                      pg.image.load("punch/4.png").convert_alpha()]
        self.walk_count = 0
        self.punch_count = 0

    def stop(self, pos):
        self.win.blit(self.stay, pos)
        self.punch_count = 0
        self.walk_count = 0

    def move(self, pos, frame):
        if self.walk_count and (15 <= frame <= 29 or 45 <= frame <= 59):
            self.win.blit(self.walk[-1], pos)
            self.walk_count -= 1
        else:
            self.win.blit(self.walk[0], pos)
            self.walk_count += 1

    def attack(self, pos, frame):
        if 0 <= frame <= 6:
            self.win.blit(self.punch[0], pos)
            self.punch_count += 1
        elif 7 <= frame <= 14:
            self.win.blit(self.punch[1], pos)
            self.punch_count += 1
        elif 15 <= frame <= 22:
            self.win.blit(self.punch[2], pos)
            self.punch_count += 1
        else:
            self.win.blit(self.punch[-1], pos)
            self.punch_count = 0
            if frame == 30:
                return False
        return True
