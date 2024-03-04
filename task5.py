import cv2
import sys
import numpy as np

def show_image(name, image):
    cv2.namedWindow(name,cv2.WINDOW_NORMAL)
    cv2.imshow(name, image)
    cv2.waitKey(0)


if __name__ == '__main__':
    image = None
    try:
        image = cv2.imread(sys.argv[1])
        # image = cv2.imread("./data/images/pcb.jpg")
        if(image is None):
            raise Exception
    except:
        print("Неправильный путь до файла")
        exit()

    show_image("image",image)

    filtered_image = cv2.bilateralFilter(image,15,50,100)
    show_image("filtered_image",filtered_image)

    filtered_yuv_image = cv2.cvtColor(filtered_image, cv2.COLOR_RGB2YUV)
    show_image("filtered_yuv_image", filtered_yuv_image)

    filtered_yuv_image_2 = filtered_yuv_image[:, :, 2]
    show_image("filtered_yuv_image_2", filtered_yuv_image_2)

    filtered_yuv_image_2_inRange = cv2.inRange(filtered_yuv_image_2, 0, 100)
    show_image('filtered_yuv_image_2_inRange', filtered_yuv_image_2_inRange)

    contours, _ = cv2.findContours(filtered_yuv_image_2_inRange,  cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

    image1 = image.copy()
    cv2.drawContours(image1, contours, -1, (0,0,255), 5)
    cv2.fillPoly(image1,pts=[*contours],color=(0,255,0))
    show_image('drawContours', image1)

    image2 = image.copy()
    for contour in contours:
        [x,y,w,h] = cv2.boundingRect(contour)
        cv2.rectangle(image2, (x,y), (x+w,y+h), (0, 0, 255), 3)
    show_image('boundingRect', image2)

    cv2.destroyAllWindows()


