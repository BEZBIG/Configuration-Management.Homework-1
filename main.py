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

    # Переход в другую директорию
    def cd(self, path):
        new_path = os.path.join(self.current_dir, path)  # Формируем полный путь для перехода
        if os.path.isdir(new_path):  # Проверяем, является ли путь директорией
            self.current_dir = new_path  # Обновляем текущую директорию
        else:
            print(f"Error: directory {path} не does not exist")  # Выводим ошибку, если директория не найдена


    # Удаление файла или директории
    def rm(self, path):
        target_path = os.path.join(self.current_dir, path)  # Формируем полный путь для удаления
        if os.path.isfile(target_path):  # Проверяем, является ли это файлом
            os.remove(target_path)  # Удаляем файл
        elif os.path.isdir(target_path):  # Проверяем, является ли это директорией
            shutil.rmtree(target_path)  # Удаляем директорию и всё её содержимое
        else:
            print(f"Error: file or directory {path} not found")  # Сообщаем, если файл или директория не найдены

    # Копирование файла или директории
    def cp(self, src, dest):
        src_path = os.path.join(self.current_dir, src)  # Формируем путь к исходному файлу или директории
        dest_path = os.path.join(self.current_dir, dest)  # Формируем путь к месту назначения
        if os.path.exists(src_path):  # Проверяем, существует ли исходный файл или директория
            if os.path.isfile(src_path):
                shutil.copy(src_path, dest_path)  # Копируем файл
            elif os.path.isdir(src_path):
                shutil.copytree(src_path, dest_path)  # Рекурсивно копируем директорию
        else:
            print(f"Ошибка: файл или директория {src} не найдены")  # Сообщаем, если исходный объект не найден






