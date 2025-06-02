import os
import sys

def resource_path(relative_path):
    """ Для корректного поиска файлов внутри .exe """
    try:
        # PyInstaller создает временную папку, и путь к ней лежит в _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)