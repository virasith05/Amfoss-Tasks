n=int(input())

for j in range(n):
    t=int(input())
    s=0
    for i in range(1, t):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print(s)
