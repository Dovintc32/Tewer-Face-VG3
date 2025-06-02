# main.py

import pygame
import time
from Assets.asset_python.SETTINGS import *
from Assets.asset_python.SceneMinusOne import scene_minus_one

pygame.init()

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Загрузка шрифтов
font_title = pygame.font.Font(FONT_PATH, FONT_SIZE_TITLE)
font_subtitle = pygame.font.Font(FONT_PATH, FONT_SIZE_SUBTITLE)

# Состояния
scene = INITIAL_SCENE
Animate_Type = INITIAL_ANIMATION_TYPE
alpha = INITIAL_ALPHA
start_time = None

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Очистка экрана

    if scene == -1:
        if Animate_Type == 1:
            alpha += 4
            if alpha >= 255:
                alpha = 255
                Animate_Type = 0
                start_time = time.time()

        elif Animate_Type == 0:
            current_time = time.time()
            if current_time - start_time >= PAUSE_DURATION:
                Animate_Type = -1

        elif Animate_Type == -1:
            alpha -= 4
            if alpha <= 0:
                alpha = 0
                scene = 0

        # Вызываем сцену -1
        scene_minus_one(screen, font_title, font_subtitle, alpha)

    elif scene == 0:
        screen.fill((0, 0, 0))  # Пустая сцена

    pygame.display.flip()
    clock.tick(60)