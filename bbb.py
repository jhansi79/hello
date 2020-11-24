m=int(input())
for i in range(m):
    l=int(input())
    k=list(map(int,input().split(" ")))
    g=1
    s=1
    for j in range(n-1):
        if k[j+1]>k[j]:
            g+=1
            s+=g
        else:
            if g>1:
                g-=1
                s+=g
            else:
                s+=g
    print(s)
    print()