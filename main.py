import os
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

#Класс для эмуляции shell
class EmulatorShell:
    def __init__(self, config_file):
        self.current_dir = "/" # Текущий каталог
        self.file_system = {} # Виртуальная файловая система в виде словаря
        self.hostname = "localhost"  # Имя компьютера по умолчанию
        self.load_config(config_file)  # Загружаем конфигурационный файл
        self.load_filesystem()  # Загружаем виртуальную файловую систему из архива


