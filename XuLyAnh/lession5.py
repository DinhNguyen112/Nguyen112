# import cv2
#
# img = cv2.imread("D:\\HK2(2023-2024)\\XuLyAnh(TH)\\image\\hinhnen.jpg")
# cv2.imshow("image1",img)
# img1 = img.copy()
# img1_flat = img1.reshape(-1)
# Max = max(img1_flat)
# print(img.dtype)
#
# img_neg = Max-img
# cv2.imshow("image2",img_neg)
# cv2.waitKey()
# cv2.destroyWindow()

# doc anh mau, hien thi anh vua doc ra man hinh, chuyen anh grayscale theo pp lightness,average,luminosity

import cv2
import numpy as np

def rgb_to_lightness(rgb_image):
    r, g, b = cv2.split(rgb_image)
    lightness = (np.maximum(r, np.maximum(g, b)) + np.minimum(r, np.minimum(g, b))) // 2
    return lightness

def rgb_to_grayscale_average(rgb_image):
    r, g, b = cv2.split(rgb_image)
    grayscale = (r + g + b) // 3
    return grayscale

def rgb_to_luminosity(rgb_image):
    r, g, b = cv2.split(rgb_image)
    luminosity = 0.21 * r + 0.72 * g + 0.07 * b
    return luminosity.astype(np.uint8)



if __name__ == "__main__":
    image = cv2.imread("D:\\HK2(2023-2024)\\XuLyAnh(TH)\\image\\thiennhien.png", cv2.IMREAD_COLOR)
    roi = image[50:600, 50:600]
    cv2.imshow("Color", roi)
    image2 = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GreyScale", image2)
    image_lightness = rgb_to_lightness(roi)

    cv2.imshow("Lightness Grayscale", image_lightness)
    image_grayscale_average = rgb_to_grayscale_average(roi)

    cv2.imshow("Average Grayscale", image_grayscale_average)
    image_luminosity = rgb_to_luminosity(roi)
    cv2.imshow("Luminosity Grayscale", image_luminosity)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



