def InputData():
    n = int(input("n="))
    return n
def Giaithua(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s 
# def GiaiThua(n):
#     if n==0:
#         return 1
#     return n*GiaiThua(n-1)
def main():
    n=int(input("n="))
    s=Giaithua(n)
    print("%d"%n,"!=%d"%s)
if __name__=="__main__":# là một đoạn mã quan trọng trong Python, giúp xác định cách thức thực thi một tập tin Python.
    main()