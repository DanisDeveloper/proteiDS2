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

    show_image("Source", image)
    show_image("BGR", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    show_image("XYZ", cv2.cvtColor(image, cv2.COLOR_RGB2XYZ))
    show_image("HSV", cv2.cvtColor(image, cv2.COLOR_RGB2HSV))
    show_image("HLS", cv2.cvtColor(image, cv2.COLOR_RGB2HLS))
    show_image("LAB", cv2.cvtColor(image, cv2.COLOR_RGB2LAB))
    show_image("LUV", cv2.cvtColor(image, cv2.COLOR_RGB2LUV))
    show_image("YUV", cv2.cvtColor(image, cv2.COLOR_RGB2YUV))
    img = image.astype(np.float64) / 255.
    K = 1 - np.max(img, axis=2)
    C = (1 - img[..., 2] - K) / (1 - K)
    M = (1 - img[..., 1] - K) / (1 - K)
    Y = (1 - img[..., 0] - K) / (1 - K)
    CMYK_image = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
    show_image("CMYK", CMYK_image)

    r, g, b = cv2.split(image)
    show_image("R", r)
    show_image("G", g)
    show_image("B", b)

    show_image("R // 2", r // 2)
    show_image("R * 2", r * 2)
    show_image("R - 20", r - 20)
    show_image("R + 20", r + 20)

    show_image("merge(r,g,b)", cv2.merge((r, g, b)))

    show_image("blur", cv2.blur(image, (10, 10)))
    show_image("Gaussian blur", cv2.GaussianBlur(image, (7, 21), 5))
    show_image("Median blur", cv2.medianBlur(image, 11))
    show_image("Bilateral filter", cv2.bilateralFilter(image, 11, 50, 50))

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    show_image("Canny", cv2.Canny(gray_image, 20, 120))
    show_image("Laplacian", cv2.Laplacian(gray_image, cv2.CV_64F))
    show_image("Sobel horizontal", cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, 5))
    show_image("Sobel vertical", cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, 5))
    show_image("Scharr horizontal", cv2.Scharr(gray_image, cv2.CV_64F, 0, 1))
    show_image("Scharr vertical", cv2.Scharr(gray_image, cv2.CV_64F, 1, 0))

    extra = cv2.cvtColor(image, cv2.COLOR_RGB2YUV)
    extra = cv2.bilateralFilter(extra, 15, 50, 70)
    extra = cv2.Canny(extra, 20, 123)
    show_image("extra", extra)

    cv2.destroyAllWindows()
