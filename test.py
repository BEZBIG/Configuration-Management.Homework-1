import pytest
import os
import zipfile
import xml.etree.ElementTree as ET
from main import EmulatorShell


def test_ls():
    emulator = EmulatorShell('config.xml')
    # Перенаправляем вывод в строку для тестирования
    from io import StringIO
    import sys
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    emulator.ls()
    output = sys.stdout.getvalue().strip().split('\n')
    sys.stdout = old_stdout

    assert sorted(output) == sorted(['Left', 'Right', 'main.js'])


def test_cd():
    emulator = EmulatorShell('config.xml')
    emulator.cd('Left')
    assert emulator.current_dir == emulator.fs_structure['Left']
    assert emulator.path == '/Left'

    emulator.cd('..')
    assert emulator.current_dir == emulator.fs_structure
    assert emulator.path == '/'

    # Тестирование ошибки перехода в несуществующую директорию
    emulator.cd('non_existent')
    assert emulator.path == '/'


def test_rm():
    emulator = EmulatorShell('config.xml')
    emulator.cd('Left')
    emulator.rm('file1.txt')
    assert 'file1.txt' not in emulator.current_dir
    emulator.rm('non_existent')  # тестируем удаление несуществующего файла


def test_cp():
    emulator = EmulatorShell('config.xml')
    emulator.cd('Left')
    emulator.cp('file1.txt', 'file1_copy.txt')
    assert 'Left.gif' in emulator.current_dir


if __name__ == '__main__':
    pytest.main()