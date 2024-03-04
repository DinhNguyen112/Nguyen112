#Viet ctr dat vao hinh rgb(img1) chuyen ve bgr(img2)
# viet img2 ra dia cung
# import cv2
#
#
# img1 = cv2.imread("D:\\HK2(2023-2024)\\XuLyAnh(TH)\\image\\hinhnen.jpg",cv2.IMREAD_COLOR)
# cv2.imshow("image1",img1)
# img2 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
# cv2.imwrite("D:\\HK2(2023-2024)\\XuLyAnh(TH)\\image\\hinhnen2.jpg",img2)
# cv2.waitKey(0)
# # hold the window
# cv2.destroyWindow()

import cv2
import numpy as np

image = cv2.imread("D:\\HK2(2023-2024)\\XuLyAnh(TH)\\image\\RGB_paint.png")
R,G,B = cv2.split(image)
# Corresponding channels are separated
zeros = np.zeros(R.shape,np.uint8)
redBGR = cv2.merge([zeros,zeros,R])
greenBGR = cv2.merge([zeros,G,zeros])
blueBGR = cv2.merge([B,zeros,zeros])
cv2.imshow("original", image)
cv2.imshow("red", redBGR)
cv2.imshow("Green", greenBGR)
cv2.imshow("blue", blueBGR)






cv2.waitKey(0)

cv2.destroyAllWindows()