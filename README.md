# Проект по Data Science для ГК Протей

## Быстрая настройка для Windows
```
git clone https://github.com/DanisDeveloper/proteiDS2.git
cd proteiDS2
python -m venv venv
venv\Scripts\activate.bat
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
```
## Быстрая настройка для Linux
```
git clone https://github.com/DanisDeveloper/proteiDS2.git
cd proteiDS2
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```
## Задание №3 находится в task3.py
```
python task3.py ./data/images/pcb.jpg
```

## Результат
Вывод в консоль изображения, его разрешения и количество каналов, также вывод разрешения масштабированного изображения, значения цвета центрального пикселя обрезанного изображения.
Отрисовка 11 окон с различными изменениями изображения.
Нажатие на любую клавишу закрывает все окна.

## Задание №4 находится в task4.py
```
python task4.py ./data/images/pcb.jpg
```

## Результат
Отрисовка 26 окон с применением различных цветовых пространств, низкочастотных и высокочастотных фильтров.
Нажатие на любую клавишу закрывает все окна.