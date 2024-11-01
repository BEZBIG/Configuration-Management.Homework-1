Проект командной строки

https://github.com/BEZBIG/Configuration-Management.Homework-1

Задание:

Разработать эмулятор для языка оболочки ОС. Необходимо сделать работу
эмулятора как можно более похожей на сеанс shell в UNIX-подобной ОС.
Эмулятор должен запускаться из реальной командной строки, а файл с
виртуальной файловой системой не нужно распаковывать у пользователя.
Эмулятор принимает образ виртуальной файловой системы в виде файла формата
zip. Эмулятор должен работать в режиме CLI.

Конфигурационный файл имеет формат xml и содержит:

• Имя компьютера для показа в приглашении к вводу.

• Путь к архиву виртуальной файловой системы.

Необходимо поддержать в эмуляторе команды ls, cd и exit, а также
следующие команды:

1. rm.
2. cp.

Все функции эмулятора должны быть покрыты тестами, а для каждой из
поддерживаемых команд необходимо написать 3 теста.

Структура файлов в проекте:

test.zip - Архив, с которым мы будем работать, в нём содержится несколько папок и файлов (Left, Right...)

config.xml - Конфигурационный файл, содержит 2 параметра(hostname, filesystem)

main.py - Главный файл программы, в котором мы выгружаем содержимое архива во временную папку и работаем с ней, а также оперируем вызовом команд ls, cd, rm, cp и exit

test.py - Файл программы, который тестирует работоспособность командной строки

Описание команд CLI:

ls - просмотр содержимого директорий

cd - переход в другую директорию

rm - удаление файла

cp - копирование файла

exit - прерывание работы эмулятора

Работа с эмулятором : 

![Image alt1](https://github.com/BEZBIG/Configuration-Management.Homework-1/blob/master/pictures/1.png)

![Image alt2](https://github.com/BEZBIG/Configuration-Management.Homework-1/blob/master/pictures/2.png)

![Image alt3](https://github.com/BEZBIG/Configuration-Management.Homework-1/blob/master/pictures/3.png)

![Image alt4](https://github.com/BEZBIG/Configuration-Management.Homework-1/blob/master/pictures/4.png)

![Image alt5](https://github.com/BEZBIG/Configuration-Management.Homework-1/blob/master/pictures/5.png)

![Image alt6](https://github.com/BEZBIG/Configuration-Management.Homework-1/blob/master/pictures/6.png)


Тесты программы :

![Image alt7](https://github.com/BEZBIG/Configuration-Management.Homework-1/blob/master/pictures/7.png)

![Image alt8](https://github.com/BEZBIG/Configuration-Management.Homework-1/blob/master/pictures/8.png)

Оперируем с тестовым файлом и проводим проверку:

![Image alt9](https://github.com/BEZBIG/Configuration-Management.Homework-1/blob/master/pictures/9.png)

