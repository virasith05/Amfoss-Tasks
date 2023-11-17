x = []
z = []

first_digit = None
smallest = None
smallest_found = False
first_added = False

t = int(input())

for q in range(t):
    first_digit = None
    smallest = None
    smallest_found = False
    first_added = False
    useless_input = input()
    y = list(map(int, input().split()))
    
    z = [0] * len(y)
    x = []
   
    first_digit = y[0]
    last_x = x[-1] if x else 0
    
    for i, elem in enumerate(y):
        
        if first_added:

            if smallest_found: 
                if smallest <= elem <= first_digit:
                    x.append(elem)
                    smallest = elem
                    z[i] = 1

            if not smallest_found:
                if elem <= first_digit:
                    x.append(elem)
                    last_x = elem
                    smallest = elem
                    smallest_found = True
                    z[i] = 1

            if not smallest_found:
                if elem >= last_x:
                    x.append(elem)
                    last_x = elem
                    z[i] = 1

        if not first_added:
            x.append(elem)
            first_added = True
            first_digit = elem
            last_x = elem
            z[i] = 1
    
    binary = ''.join(str(item) for item in z)

    print(binary)

