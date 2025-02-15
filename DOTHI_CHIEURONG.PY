import os # Nhập module os, nhưng trong mã này không sử dụng

G = [] # Khởi tạo danh sách rỗng G, sẽ được dùng để lưu ma trận kề của đồ thị

# Hàm Init dùng để khởi tạo ma trận kề từ file đầu vào
def Init(path, G):
    f = open(path) # Mở file đường dẫn path để đọc
    n = int(f.readline(), base=10) # Đọc dòng đầu tiên từ file, chuyển thành số nguyên n (số đỉnh của đồ thị)

    # Khởi tạo ma trận kề kích thước (n+1)x(n+1) với giá trị ban đầu là 0
    for i in range(n+1): 
        G.append([]) # Thêm hàng mới vào ma trận G
        for j in range(n+1):
            G[i].append(0) # Thêm cột mới, giá trị ban đầu là 0

    # Đọc từng dòng trong file để lấy các cạnh của đồ thị
    while True:
        string = f.readline() # Đọc một dòng từ file
        if not string: # Nếu dòng rỗng, dừng việc đọc file
            break
        string = string.replace('\t', ' ') # Thay thế ký tự tab bằng khoảng trắng

        # Tìm vị trí của khoảng trắng đầu tiên
        k = string.index(' ')
        # Lấy số đầu tiên (đỉnh thứ nhất của cạnh)
        str = string[0:k]
        i = int(str)

        # Tìm vị trí của khoảng trắng tiếp theo
        m = string.index(' ', k+1, -1)
        # Lấy số thứ hai (đỉnh thứ hai của cạnh)
        str = string[k+1:m]
        j = int(str)

        # Lấy trọng số của cạnh giữa đỉnh i và j
        str = string[m+1:len(string)]
        x = int(str)

        # Gán giá trị trọng số cho cả G[i][j] và G[j][i] vì đồ thị vô hướng
        G[i][j] = G[j][i] = x

    f.close() # Đóng file sau khi đọc xong
    return n # Trả về số đỉnh của đồ thị

# Hàm ViewMatrix để in ra ma trận kề của đồ thị
def ViewMatrix(G, n):
    for i in range(1, n+1): # Duyệt qua các đỉnh từ 1 đến n
        for j in range(1, n+1):
            print("%d" % G[i][j], end=' ') # In từng phần tử trong ma trận, cách nhau bằng khoảng trắng
        print() # Xuống dòng sau mỗi hàng của ma trận

# Hàm BFS để duyệt đồ thị theo thuật toán tìm kiếm theo chiều rộng (Breadth-First Search)
def BFS(u, n):
    Q = [] # Hàng đợi để quản lý các đỉnh chờ xử lý
    C = [] # Danh sách để đánh dấu đỉnh nào đã được duyệt

    # Khởi tạo Q và C với n+1 phần tử là 0 (tương ứng với số đỉnh)
    for j in range(n+1):
        Q.append(0)
        C.append(0)

    # Khởi tạo hàng đợi
    first = 1; last = 1
    Q[last] = u # Thêm đỉnh u vào hàng đợi
    C[u] = 1   # Đánh dấu đỉnh u đã được duyệt

    # Vòng lặp BFS, duyệt hàng đợi cho đến khi rỗng
    while first <= last:
        u = Q[first]; first += 1 # Lấy đỉnh từ đầu hàng đợi và tăng chỉ số first
        print("%d" % u, end='\t') # In đỉnh hiện tại

        # Duyệt qua tất cả các đỉnh v
        for v in range(1, n+1):
            # Nếu có cạnh giữa u và v và v chưa được duyệt
            if G[u][v] != 0 and C[v] == 0:
                last += 1 # Thêm đỉnh v vào cuối hàng đợi
                Q[last] = v
                C[v] = 1 # Đánh dấu v đã được duyệt

# Hàm main, là điểm bắt đầu của chương trình
def main():
    # Khởi tạo đồ thị từ file Graph.inp và trả về số đỉnh n
    n = Init("Graph.inp", G)
    
    print("Xem ma trận G:", end='\n')
    # In ma trận kề của đồ thị
    ViewMatrix(G, n)

    # Chạy thuật toán BFS từ đỉnh 4
    u = 4; BFS(u, n) # In kết quả dự kiến: 4 2 5 1 3 6

# Điểm bắt đầu của chương trình khi file này được chạy
if __name__ == "__main__":
    main()






