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

    # Загружаем конфигурацию из XML-файла
    def load_config(self, config_file):
        tree = ET.parse(config_file)  # Парсим XML-файл
        root = tree.getroot()  # Получаем корневой элемент
        self.hostname = root.find("hostname").text  # Извлекаем имя компьютера
        self.fs_path = root.find("filesystem").text  # Извлекаем путь к файловой системе

    # Загружаем файловую систему из ZIP-архива
    def load_filesystem(self):
        with zipfile.ZipFile(self.fs_path, 'r') as zip_ref:  # Открываем ZIP-архив
            for file in zip_ref.namelist():  # Для каждого файла в архиве
                self.file_system[file] = zip_ref.read(file)  # Сохраняем содержимое файла в словарь