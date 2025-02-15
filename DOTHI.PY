import os
G = []

def Init(path, G):
    f = open(path)
    n = int(f.readline(), base=10)
    for i in range(n + 1):
        G.append([])
    for i in range(n + 1):
        G[i].append(0)

    while True:
        string = f.readline()
        if not string:
            break
        string = string.replace('\t', '')

        k = string.index('')
        str_i = string[0:k]
        i = int(str_i,base=10)
        m = string.index(' ', k + 1)
        str_j = string[k + 1:m]
        j = int(str_j,base=10)
        str_x = string[m + 1:len(string)]
        x = int(str_x,base=10)
        G[i][j] = G[j][i] = x

    f.close()
    return n

def ViewMatrix(G, n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("%d" % G[i][j], end='')
        print()

def main():
    n = Init("grash.inp", G)
    print("Xem ma trận G:")
    ViewMatrix(G, n)

if __name__ == "__main__":
    main()
