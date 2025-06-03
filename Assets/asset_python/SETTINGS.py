# SETTINGS.py
import sys
import os

# Получаем путь к текущему файлу (SS.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Поднимаемся на уровень выше (в корень проекта)
project_root = os.path.dirname(current_dir)
# Добавляем корень в системный путь
if project_root not in sys.path:
    sys.path.append(project_root)
from Assets.asset_python.EXEhelper import resource_path



# Размер окна
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Пути к ресурсам
FONT_PATH = resource_path("Assets/other/Bold.ttf")
FONT_SIZE_TITLE = 100
FONT_SIZE_SUBTITLE = 50

# Начальное состояние
INITIAL_SCENE = -1
INITIAL_ANIMATION_TYPE = 1
INITIAL_ALPHA = 0
PAUSE_DURATION = 1  # секунд