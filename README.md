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
## Точка входа в программу находится в task3.py
```
python main.py ./data/images/pcb.jpg
```

## Результат
Вывод в консоль изображения, его разрешения и количество каналов, также вывод разрешения масштабированного изображения, значения цвета центрального пикселя обрезанного изображения.
Отрисовка 11 окон с различными изменениями изображения.
Нажатие на любую клавишу закрывает все окна.
