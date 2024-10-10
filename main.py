import os
import zipfile
import xml.etree.ElementTree as ET
import shutil # Модуль для операций копирования и удаления файлов и директорий

#Класс для эмуляции shell
class EmulatorShell:
    def __init__(self, config_file):
        # Чтение конфигурационного файла XML
        tree = ET.parse(config_file)
        root = tree.getroot()

        # Получение имени компьютера из конфигурации
        self.hostname = root.find('hostname').text

        # Получение пути к zip-архиву виртуальной файловой системы
        self.fs_zip_path = root.find('filesystem').text

        # Временная директория для файловой системы
        self.temp_files_path = '/tmp/test_files'

        # Текущая директория в файловой системе
        self.current_dir = self.temp_files_path

        # Распаковка файловой системы
        self.extract_files()

    # Распаковка zip-архива виртуальной файловой системы во временную директорию.
    def extract_files(self):
        if os.path.exists(self.temp_files_path):
            shutil.rmtree(self.temp_files_path)  # Удаляем предыдущие данные, если они существуют
        os.makedirs(self.temp_files_path)  # Создаем временную директорию

        with zipfile.ZipFile(self.fs_zip_path, 'r') as zip_ref:
            zip_ref.extractall(self.temp_files_path)  # Распаковка файлов в temp_files_path

    # Вывод содержимого текущей директории
    def ls(self):
        try:
            for item in os.listdir(self.current_dir): # Получаем список файлов и директорий в текущей директории
                print(item) # Выводим каждый элемент
        except FileNotFoundError:
            print("Error: directory not found")






