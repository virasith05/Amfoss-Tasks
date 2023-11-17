n=int(input())
g=list(map(int,input('').split()))
v=g.copy()
g.sort()

if(g[0]==g[1]):
    print("Still Aetheria")
else:
    print((v.index(min(v)))+1)


