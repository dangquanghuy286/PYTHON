def InPutData():
    a=int(input("Nhap a="))
    b=int(input("Nhap b="))
    return a,b
def UCLN(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else :
            b=b-a
    return a

def main():
    a,b=InPutData()
    c =UCLN(a,b)
    print("UCLN=%d"%c)
if __name__=="__main__":# là một đoạn mã quan trọng trong Python, giúp xác định cách thức thực thi một tập tin Python.
    main()