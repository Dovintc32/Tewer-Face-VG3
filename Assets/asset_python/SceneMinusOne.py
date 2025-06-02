# SceneMinusOne.py

import pygame

def scene_minus_one(screen, font_title, font_subtitle, alpha):
    # Рендерим текст
    text_surface = font_title.render("Tewer Face", True, (255, 0, 0))
    text_surface2 = font_subtitle.render("Dovintc and Toock1k", True, (255, 255, 255))

    # Создаем прозрачные поверхности
    transparent_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
    transparent_surface.blit(text_surface, (0, 0))
    transparent_surface.set_alpha(alpha)

    transparent_surface2 = pygame.Surface(text_surface2.get_size(), pygame.SRCALPHA)
    transparent_surface2.blit(text_surface2, (0, 0))
    transparent_surface2.set_alpha(alpha)

    # Центрируем текст
    text_rect = transparent_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 40))
    text_rect2 = transparent_surface2.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 40))

    # Отрисовываем
    screen.blit(transparent_surface, text_rect)
    screen.blit(transparent_surface2, text_rect2)