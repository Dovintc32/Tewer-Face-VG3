import sys
import os

# Получаем путь к текущему файлу (Assets/Test/SS.py)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Поднимаемся на 2 уровня выше — до корня проекта
project_root = os.path.dirname(os.path.dirname(current_dir))

# Добавляем корень в sys.path
if project_root not in sys.path:
    sys.path.append(project_root)
    print(f"📎 Добавили корень в sys.path: {project_root}")

from Assets.asset_python.SETTINGS import *

# Здесь можно продолжить остальной код