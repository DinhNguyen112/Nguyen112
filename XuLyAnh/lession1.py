def KhoiTao():

    a = int(input("Nhâp giá trị của a: "))
    b = int(input("Nhâp giá trị của b: "))
    c = int(input("Nhâp giá trị của c: "))

    return a, b, c
def HienThi(a , b , c):
    print("Hiển thị giá trị vừa nhập: ",a,b,c)
def Tong(a , b, c ):
    tong = a + b + c
    print("Tổng của 3 số: ", tong)
def MaxMin(a,b,c):
    min_value = min(a, b, c)
    max_value = max(a, b, c)

    print("Giá trị nhỏ nhất là:", min_value)
    print("Giá trị lớn nhất là: ", max_value)
    return min_value,max_value
def TimKiem(a,b,c ,x ):

    if x in (a,b,c):
        print(f"Số {x} có trong các số a,b,c")
    else:
        print(f"Số {x} không có trong các số a,b,c")
if __name__ == '__main__':

    a,b,c = KhoiTao()
    HienThi(a,b,c)
    Tong(a,b,c)
    MaxMin(a,b,c)
    x = int(input("Nhập giá trị x cần tìm: "))
    TimKiem(a,b,c,x)

