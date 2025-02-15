import math
def InPutDaTa():
    a=float(input("a="))
    b=float(input("b="))
    c=float(input("c="))
    return a,b,c
def XuLy(a,b,c):
    if a==0 and b==0 and c==0:
        print("Vo So  Nghiem")
    elif a==0 and b==0 and c!=0:
        print("Vo Nghiem")
    elif a==0 and b!=0:
        x=-c/b
        print("Ptb1 : X= ",str(x))
    else:
        delta=math.pow(b,2) - 4*a*c
        if delta > 0:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            print("PT CO 2 NGHIEM PHAN BIET\n")
            print("x1=%.3lf"%x1,"x2=%.3lf"%x2)
        elif delta == 0:
            x0=-b/(2*a)
            print("NGHIEM KEP:\n")
            print("x0=%.2lf"%x0)
        else:
            print("NGHIEM THUC")
def main():
    a,b,c=InPutDaTa()

    XuLy(a,b,c)
if __name__=="__main__":# là một đoạn mã quan trọng trong Python, giúp xác định cách thức thực thi một tập tin Python.
    main()            
            

