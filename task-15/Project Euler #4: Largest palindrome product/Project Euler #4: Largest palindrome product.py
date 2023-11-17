def is_palindrome(n):
    return str(n) == str(n)[::-1]

l=[]

for i in range(100,1000):
    for j in range(100,i+1):
        p=i*j
        if is_palindrome(p):
            l.append(p)
l.sort(reverse=True)

t = int(input())
for _ in range(t):
    n = int(input())
    for i in l:
        if i<n:
            print(i)
            break
