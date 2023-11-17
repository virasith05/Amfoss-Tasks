import math
t=int(input())

for j in range(t):
    n=int(input())
    
    def lcm(a, b):
        return a * b // math.gcd(a, b)

    result=1
    
    for i in range(2,n + 1):
        result=lcm(result, i)

    print(result)
