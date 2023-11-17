t=int(input())

for i in range(t):
    word="amfoss"
    a=input()
    differnet=0
    for i in range(len(word)):
        if word[i]!=a[i]:
            differnet+=1
    print(differnet)