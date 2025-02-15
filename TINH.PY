#PHEP TOAN 
import math
def InputData():
    a=int(input("a="))
    b=int(input("b="))
    return a,b
def Tong(a,b):
    c=a+b
    return c
def Hieu(a,b):
    c=a-b
    return c
def Tich(a,b):
    c=a*b
    return c
def Thuong(a,b):
    if b==0:
        print("KHONG THE CHIA 0")
        exit()
    else:c=a/b
    return c
def main():
    a,b=InputData()
    c=Tong(a,b)
    print("Tổng : %.2f + %.2f = %.2f\n" % (a, b, c))
    c=Hieu(a,b)
    print("Hiệu : %.2f - %.2f = %.2f\n" % (a, b, c))
    c=Tich(a,b)
    print("Tích : %.2f * %.2f = %.2f\n" % (a, b, c))
    c=Thuong(a,b)
    print("Thương : %.2f / %.2f = %.2f\n" % (a, b, c))
if __name__ == "__main__":
    main()


