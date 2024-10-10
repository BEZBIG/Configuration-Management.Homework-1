import unittest
import os
from main import EmulatorShell
from pathlib import Path


class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.emulator = EmulatorShell('config.xml')

    def test_ls(self):
        self.emulator.current_dir = '/tmp/test_files'
        output = os.listdir(self.emulator.current_dir)
        self.assertIn('main.js', output)  # Тест на наличие файла

    def test_cd(self):
        self.emulator.cd('Left')
        expected_path = Path('/tmp/test_files/Left')
        self.assertEqual(Path(self.emulator.current_dir), expected_path)

    def test_rm(self):
        test_file = os.path.join(self.emulator.current_dir, 'testfile.txt')
        open(test_file, 'w').close()  # Создаем тестовый файл
        self.emulator.rm('testfile.txt')
        self.assertFalse(os.path.exists(test_file))

    def test_cp(self):
        src_file = os.path.join(self.emulator.current_dir, 'testfile.txt')
        dest_file = os.path.join(self.emulator.current_dir, 'copyfile.txt')
        open(src_file, 'w').close()  # Создаем тестовый файл
        self.emulator.cp('testfile.txt', 'copyfile.txt')
        self.assertTrue(os.path.exists(dest_file))


if __name__ == '__main__':
    unittest.main()
