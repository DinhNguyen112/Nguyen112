import numpy as np
# arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[10, 20, 30],[40, 50, 60],[70, 80 ,90]]])
# print(arr.ndim)
# print(arr.shape)
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(A[0:6])
# print(A[::])
# print(A[-4:-1])
# print(A[-3:])
# print(A[:-1])
# print(A[::2])
print(A[::2])
#
# print(np.where(A%2!=0))
# Ar= np.array([1,3,5,7,9])
# X = Ar.searchsorted(6)
# print(X)
# X = Ar.searchsorted(7,side='right')
# print(X)
# A2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# A2_2d = A2.reshape(2,-1) # cho -1 xac dinh tùy ý theo kích thước của mảng vd dụ 2 hàng - 4 cột
# A2_3d = A2.reshape(2, 2, 2)
# A2_3d = A2.reshape(2, 4, 1)
# #print(A2_2d)
# print(A2_3d)
# B = A2.reshape(-1)
# print(B)


from numpy import random
x = random.randint(100, size=(5))
x0 = random.rand()
print(x0)

