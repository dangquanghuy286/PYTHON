M = [] ;n=10
def CreateArr(M, n):
    for i in range(n):
        M.append(int(input('Nhập Số thứ %d: ' % (i+1))))
def ViewArr(M,n):
    for i in range(n):
        print("%d \t "%M[i],end=' ')
    print()            
def SumArr(M,n):
    s=0
    for i in range(n):
        s+=int(M[i])
    return s
def SumLe(M,n):
    s=0
    for i in range(n):
        if int(M[i]) % 2!=0:
            s+=int(M[i])
    return s
def SortArr(M,n):
    for i in range(n):
        for j in range(n):
            if int(M[j]) > int(M[i]):
                temp =M[i];M[i]=M[j];M[j]=temp 
def DeleteArr(M,n,k):
    for i in range(k,n-1):
        M[i]=M[i+1]
    n-=1    
    return n
def InsertArr(M,n,k,x):
    for i in range(k,n,-1):
        M[i]=M[i-1]
    M[k]=x;n+=1   
    return n
def InPut(x):
    try:
        n=int(input("Nhập"+x+": "))
        if n<=0:
            exit()
        return n
    except:
        print('Phai nhap so tu nhien')
        exit()
def main():
    n = InPut(" số lượng phần tử")  # Nhắc người dùng nhập số lượng phần tử
    CreateArr(M, n)  # Tạo mảng
    print("Mảng vừa nhập là:")
    ViewArr(M, n)  # Xem mảng
    
    sum_odd = SumLe(M, n)  # Tổng các số lẻ
    print(f"Tổng các số lẻ trong mảng: {sum_odd}")
    
    SortArr(M, n)  # Sắp xếp mảng
    print("Mảng sau khi sắp xếp:")
    ViewArr(M, n)
    
    # Ví dụ xóa một phần tử
    k = InPut(" vị trí muốn xóa") - 1  # Nhận chỉ số cần xóa
    n = DeleteArr(M, n, k)
    print(f"Mảng sau khi xóa phần tử tại vị trí {k + 1}:")
    ViewArr(M, n)
    
    # Ví dụ chèn một phần tử
    x = InPut(" giá trị muốn chèn")
    k = InPut(" vị trí muốn chèn") - 1
    n = InsertArr(M, n, k, x)
    print(f"Mảng sau khi chèn {x} vào vị trí {k + 1}:")
    ViewArr(M, n)

if __name__=="__main__":# là một đoạn mã quan trọng trong Python, giúp xác định cách thức thực thi một tập tin Python.
    main()       