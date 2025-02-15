import os
G=[];
P=[];
n=0;
def Split(string):
    k=string.index('');str=string[0:k]
    a=int(str);m=string.index('',k+1,-1);str=string[k+1:m]
    b=int(str);str=string[m+1:len(string)]
    c=int(str)
    return a,b,c
def Init(path, G):
    f = open(path)
    string = f.readline()
    n,s,g=Split(string.replace('\t',''))
    for i in range(n + 1):
        G.append([])
        for j in range(n + 1):
            G[i].append(0)

    while True:
        string=f.readline()
        if not string:
            break
        i,j,x=Split(string.replace('\t',''))
        G[i][j]=G[j][i]=x
    f.close()
    return n,s,g

#------------------------------------------------------------#
def Breadth_First_Search(G,n,s,g,P):
    Open=[];Close=[]
    for j in range(n+1):
        Open.append(0)
        Close.append(0)
        P.append(0)
    front=1; rear=1; Open[rear]=s
    P[s]=s;
    while(front<=rear):
        u=Open[front];front+=1
        if u ==g :
            return 1
        for v in range(1,n+1):
            if G[u][v] !=0 and not v in Open and not v in Close:
                rear+=1;Open[rear]=v;P[v]=u;
        Close[u]=u;
    return 0; 
#---------------------------------------------------------------------------
def Print(P,n,s,g):
    Path=[]
    for i in range(0,n+1):
        Path.append(0)
    print("Duong di tu %d"%s,"den %d"%g,"la\n",end='');
    Path[0]=g
    i=P[g];k=1
    while i !=s:
        Path[k]=i;k+=1
        i=P[i]
    Path[k] =s
    for j in range(0,k+1):
        i=k-j
        if i>0:
            print("%d =>"%Path[i],end='')
        else:
            print("%d"%Path[i],end='')
#_____________________________________________________
def main():
    n,s,g= Init("GraphChieuSau.inp", G)
    Breadth_First_Search(G,n,s,g,P)
    Print(P,n,s,g)

if __name__ == "__main__":
    main()    