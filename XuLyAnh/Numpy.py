import numpy as np
#C1

# arr = np.arange(10, 101)
# print(arr)
#C2

# arr = np.arange(10, 101,2)
# print(arr)
#C3

# random_array = np.random.randn(50)
# print(random_array)
#C4

# x = np.zeros((5,10))
# x[1:-1,1:-1] = 1
# print(x)
#C5

# # Tạo ma trận 7x7 với các phần tử đường chéo chính là 1, 3, 5, 7, 9, 11, 13
# diagonal_values = np.array([1, 3, 5, 7, 9, 11, 13])
# matrix = np.diag(diagonal_values, k=0)  # k=0 để thay đổi đường chéo chính
# print(matrix)
#C6

# Tạo mảng 3x3 với các giá trị tùy ý
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Lưu mảng vào file văn bản (text)
np.savetxt("D:\\HK2(2023-2024)\\XuLyAnh(TH)\\c6numpy.txt", my_array)
# Lưu mảng vào file nhị phân (binary)
np.save('my_array_binary.npy', my_array)