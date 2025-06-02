import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)

text_color = (255, 255, 255)  # Белый цвет
alpha = 128  # Полупрозрачный

# Рендерим текст с антиалиасингом
text_surface = font.render("Прозрачный Текст", True, text_color)

# Создаем новую поверхность с SRCALPHA
transparent_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
transparent_surface.blit(text_surface, (0, 0))  # Копируем текст на неё
transparent_surface.set_alpha(alpha)  # Устанавливаем прозрачность

alpha = 0
direction = 2

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновляем alpha
    alpha += direction
    if alpha <= 0 or alpha >= 255:
        direction *= -1

    # Пересоздаем прозрачную поверхность каждый кадр
    transparent_surface = pygame.Surface(text_surface.get_size(), pygame.SRCALPHA)
    transparent_surface.blit(text_surface, (0, 0))
    transparent_surface.set_alpha(alpha)

    screen.fill((30, 30, 30))
    screen.blit(transparent_surface, (100, 150))
    pygame.display.flip()
    clock.tick(60)