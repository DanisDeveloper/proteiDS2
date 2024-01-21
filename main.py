import cv2
import sys


if __name__ == '__main__':
    path = sys.argv[1]

    image = cv2.imread(path)
    print(image)
    print("Разрешение(HxW):",image.shape[:2])
    print("Количество каналов:",image.shape[2])
    cv2.imshow("Image",image)

    image_resized = cv2.resize(image,(800,600),interpolation=cv2.INTER_AREA)
    print("Разрешение масштабированного изображения(HxW):", image_resized.shape[:2])

    image_rotated_copy = image.copy()
    height,width,channels = image.shape
    center = (width//2,height//2)
    rotate_matrix45 = cv2.getRotationMatrix2D(center,45,1.0)
    image_rotated45 = cv2.warpAffine(image_rotated_copy,rotate_matrix45,(width,height))
    cv2.imshow("Image_rotated45",image_rotated45)

    rotate_matrix90 = cv2.getRotationMatrix2D(center,90,1.0)
    image_rotated90 = cv2.warpAffine(image_rotated_copy,rotate_matrix90,(width,height))
    cv2.imshow("Image_rotated90",image_rotated90)

    rotate_matrix180 = cv2.getRotationMatrix2D(center,180,1.0)
    image_rotated180 = cv2.warpAffine(image_rotated_copy,rotate_matrix180,(width,height))
    cv2.imshow("Image_rotated180",image_rotated180)

    image_mirror_copy = image.copy()
    image_mirror_horizontal = cv2.flip(image,1)
    cv2.imshow("Image_mirror_horizontal",image_mirror_horizontal)
    image_mirror_vertical = cv2.flip(image,0)
    cv2.imshow("image_mirror_vertical", image_mirror_vertical)

    image_cropped = image[height//2:height//2+100,width//2:width//2+100].copy()
    cv2.imshow("Image_cropped",image_cropped)

    height_cropped,width_cropped,channels_cropped = image_cropped.shape
    center_cropped = (height_cropped//2,width_cropped//2)
    print("Центральный пиксель изображения:",image_cropped[center_cropped])
    image_cropped[center_cropped] = (0,0,255)
    cv2.imshow("Image_cropped with new center pixel",image_cropped)

    (x,y,size) = width_cropped//2, height_cropped//2, 20
    image_cropped[y:y+size,x:x+size] = (255,255,255)
    cv2.imshow("Image_cropped with new group pixels",image_cropped)

    cv2.rectangle(image_cropped,(x,y),(x+size,y+size),(0,0,255),2)
    cv2.imshow("Image_cropped with rectangle",image_cropped)

    cv2.putText(image_cropped,"rect",(x-5,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),1)
    cv2.imshow("Image_cropped with text",image_cropped)

    cv2.imwrite("./data/save/result.png",image_cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()