import math
def InputData():#dấu : sau tên hàm
    a=float(input("Nhap a="))
    b=float(input("Nhap b="))
    return a,b;
# ---------------------------------
def XuLy(a,b):
    if a==0:
        if b==0 :
            print("Vo so nghiem")
        else:
            print("Vo nghiem")
    else:
        x=-b/a
        print("Nghiem x=%.3lf"%x,end='\n')
def main():
    a,b=InputData()

    XuLy(a,b)
if __name__=="__main__":# là một đoạn mã quan trọng trong Python, giúp xác định cách thức thực thi một tập tin Python.
    main()
        
