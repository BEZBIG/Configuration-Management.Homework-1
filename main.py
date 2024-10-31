import zipfile
import os
import xml.etree.ElementTree as ET

# Класс для эмуляции shell
class EmulatorShell:
    def __init__(self, config_file):
        # Чтение конфигурационного файла XML
        tree = ET.parse(config_file)
        root = tree.getroot()

        # Получение имени компьютера из конфигурации
        self.hostname = root.find('hostname').text

        # Получение пути к zip-архиву виртуальной файловой системы
        self.fs_zip_path = root.find('filesystem').text

        # Загрузка виртуальной файловой системы из zip-архива
        self.fs_structure = {}
        self.load_fs_structure()

        # Текущая директория в файловой системе
        self.current_dir = self.fs_structure
        self.path = '/'

    # Загрузка файловой структуры из zip-архива
    def load_fs_structure(self):
        with zipfile.ZipFile(self.fs_zip_path, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                path_parts = file_info.filename.split('/')
                current_level = self.fs_structure

                # Создаем структуру директорий
                for part in path_parts:
                    if part:  # Игнорируем пустые элементы
                        if part not in current_level:
                            if file_info.is_dir():
                                current_level[part] = {}
                            else:
                                current_level[part] = None  # Файл обозначаем как None
                        current_level = current_level[part]

    # Вывод содержимого текущей директории
    def ls(self):
        if isinstance(self.current_dir, dict):
            for item in self.current_dir:
                print(item)
        else:
            print("Error: Current directory is invalid")

    # Переход в другую директорию
    def cd(self, path):
        if path == '/':
            self.current_dir = self.fs_structure
            self.path = '/'
        elif path == '..':
            if self.path != '/':
                self.path = '/'.join(self.path.split('/')[:-1]) or '/'
                self.current_dir = self.navigate_to_path(self.path)
        elif path in self.current_dir and isinstance(self.current_dir[path], dict):
            self.current_dir = self.current_dir[path]
            self.path += f'/{path}' if self.path != '/' else path
        else:
            print(f"Error: Directory {path} does not exist")

    # Удаление файла или директории (виртуально)
    def rm(self, path):
        if path in self.current_dir:
            del self.current_dir[path]
        else:
            print(f"Error: file or directory {path} not found")

    # Копирование файла или директории
    def cp(self, src, dest):
        if src in self.current_dir:
            self.current_dir[dest] = self.current_dir[src]
        else:
            print(f"Error: file or directory {src} not found")

    # Функция для перехода к определенной директории по пути
    def navigate_to_path(self, path):
        current = self.fs_structure
        if path == '/':
            return current
        for part in path.strip('/').split('/'):
            if part in current and isinstance(current[part], dict):
                current = current[part]
            else:
                return None
        return current

    # Основной цикл эмулятора
    def run(self):
        while True:
            # Формируем приглашение командной строки
            prompt = f'{self.hostname}:{self.path}> '
            command = input(prompt)

            if command == 'exit':
                break
            elif command.startswith('ls'):
                self.ls()
            elif command.startswith('cd'):
                path = command.split(' ')[1] if len(command.split(' ')) > 1 else '/'
                self.cd(path)
            elif command.startswith('rm'):
                path = command.split(' ')[1]
                self.rm(path)
            elif command.startswith('cp'):
                parts = command.split(' ')
                src, dest = parts[1], parts[2]
                self.cp(src, dest)
            else:
                print("The command was not recognized")

if __name__ == "__main__":
    emulator = EmulatorShell('config.xml')
    emulator.run()
