import cv2
import sys

if __name__ == '__main__':
    image = None
    try:
        image = cv2.imread(sys.argv[1])
    except:
        print("Неправильный путь до файла")
        exit()
