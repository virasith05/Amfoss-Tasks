n = int(input())
total_vector = [0, 0, 0]

for i in range(n):
    xi, yi, zi = map(int, input().split())
    total_vector[0] += xi
    total_vector[1] += yi
    total_vector[2] += zi

if total_vector == [0, 0, 0]:
    print("YES")
else:
    print("NO")