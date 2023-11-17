t = int(input())

for qwert in range (t):


    len_inp = int(input())
    input_list = list(map(int, input().split()))

    a =[]
    b =[]

    koshy = sorted(input_list) 


    last_a = koshy[0]

    a.append(last_a)

    for i in range(1, len_inp):
        j = koshy[i]
        if j == last_a:
            b.append(j)
            first_b=b[0]
        else :
            a.append(j)
            last_a = j



    for i in range (1000, -1, -1):
        if i not in a:
            snit_a = i



    for i in range (1000, -1, -1):
        if i not in b:
            snit_b = i




    result = int(snit_a)+int(snit_b)

    print(result)