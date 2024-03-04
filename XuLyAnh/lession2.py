def KhoiTao():
    list = [1,2,3,4,5,6,7,8,9,10];
    return list
def HienThi(list):
    print("List la: " ,list[0:10])
def TongPhanTu(list):
    tong = sum(list)
    print("Tổng của các phần tử trong list: ", tong)
def MaxMin(list):
    Max = max(list)
    Min = min(list)
    print("Giá trị Max trong List: ", Max)
    print("Giá trị Min trong List: ", Min)
    return Max,Min
def TimKiem(list,x):
    dem = list.count(x)
    if x in list:
        print(f"Số lần xuất hiện của số {x} trong List là: {dem} ")
    else:
        print(f"Không xuất hiện trong List")
if __name__ == '__main__':
    list = KhoiTao()
    HienThi(list)
    TongPhanTu(list)
    MaxMin(list)
    x = int(input("Nhập x cần tìm: "))
    TimKiem(list,x)

