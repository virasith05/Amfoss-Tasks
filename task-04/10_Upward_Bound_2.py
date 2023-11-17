t = int(input())

for i in range(t):
    n = int(input())
    input_list = list(map(int, input().split()))

    operations = 0
    possible = True

    for i in range (n-2, -1, -1):

        if input_list[i]>=input_list[i+1]:
            possible = True
           
            while input_list[i]>=input_list[i+1]:
                if possible:
                    input_list[i] //= 2
                    operations += 1

                    if input_list[i] == input_list [i+1] and input_list[i] == 0:
                         possible = False
                         operations = 0
                         operations -= 1
                else:
                    break
    print(operations)