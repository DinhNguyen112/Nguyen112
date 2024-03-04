import cv2
import numpy as np
image = cv2.imread("D:\\HK2(2023-2024)\\XuLyAnh(TH)\\image\\thiennhien.png", cv2.IMREAD_COLOR)
roi = image[50:600, 50:600]
# cv2.imshow("Color", roi)
image2 = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
cv2.imshow("GreyScale", image2)
image_hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", image_hsv)
print(image_hsv.shape)
V= image_hsv[:, :, 2]#lấy tất cả kênh 2
print(V)

# cv2.imshow("V chanel", V)
(_,maxVal,_,_) = cv2.minMaxLoc(V)

print("Gía trị mức sáng lớn nhất trong kênh V: ",maxVal)
cv2.waitKey(0)
cv2.destroyAllWindows()