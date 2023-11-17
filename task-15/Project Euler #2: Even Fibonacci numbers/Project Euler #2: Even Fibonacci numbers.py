t=int(input())

for i in range(t):
    n=int(input())
    a,b =0,1
    s=0

    while a<= n:
        if a%2==0:
            s+=a
        a,b=b,a+b

    print(s)