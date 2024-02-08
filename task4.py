import cv2
import sys
import numpy as np

if __name__ == '__main__':
    image = None
    try:
        image = cv2.imread(sys.argv[1])
        # image = cv2.imread("./data/images/pcb.jpg")
    except:
        print("Неправильный путь до файла")
        exit()

    cv2.imshow("Source", image)
    cv2.imshow("BGR", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    cv2.imshow("XYZ", cv2.cvtColor(image, cv2.COLOR_RGB2XYZ))
    cv2.imshow("HSV", cv2.cvtColor(image, cv2.COLOR_RGB2HSV))
    cv2.imshow("HLS", cv2.cvtColor(image, cv2.COLOR_RGB2HLS))
    cv2.imshow("LAB", cv2.cvtColor(image, cv2.COLOR_RGB2LAB))
    cv2.imshow("LUV", cv2.cvtColor(image, cv2.COLOR_RGB2LUV))
    cv2.imshow("YUV", cv2.cvtColor(image, cv2.COLOR_RGB2YUV))
    img = image.astype(np.float64) / 255.
    K = 1 - np.max(img, axis=2)
    C = (1 - img[..., 2] - K) / (1 - K)
    M = (1 - img[..., 1] - K) / (1 - K)
    Y = (1 - img[..., 0] - K) / (1 - K)
    CMYK_image = (np.dstack((C, M, Y, K)) * 255).astype(np.uint8)
    cv2.imshow("CMYK", CMYK_image)

    r, g, b = cv2.split(image)
    cv2.imshow("R", r)
    cv2.imshow("G", g)
    cv2.imshow("B", b)

    cv2.imshow("R // 2", r // 2)
    cv2.imshow("R * 2", r * 2)
    cv2.imshow("R - 20", r - 20)
    cv2.imshow("R + 20", r + 20)

    cv2.imshow("merge(r,g,b)", cv2.merge((r, g, b)))

    cv2.imshow("blur", cv2.blur(image, (10, 10)))
    cv2.imshow("Gaussian blur", cv2.GaussianBlur(image, (7, 21), 5))
    cv2.imshow("Median blur", cv2.medianBlur(image, 11))
    cv2.imshow("Bilateral filter", cv2.bilateralFilter(image, 11, 50, 50))

    cv2.imshow("Canny", cv2.Canny(image, 20, 120))
    cv2.imshow("Laplacian", cv2.Laplacian(image, cv2.CV_64F))
    cv2.imshow("Sobel", cv2.Sobel(image, cv2.CV_64F, 0, 1, 5))
    cv2.imshow("Scharr", cv2.Scharr(image, cv2.CV_64F, 1, 0))

    cv2.imshow("extra", cv2.Canny(cv2.bilateralFilter(cv2.cvtColor(image, cv2.COLOR_RGB2YUV), 15, 50, 70), 20, 123))

    cv2.waitKey(0)
    cv2.destroyAllWindows()