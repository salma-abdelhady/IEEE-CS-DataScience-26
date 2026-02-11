n = int(input())

for i in range(1, 10):
    if i * n % 4 == 0:
        continue
    print(i * n, end= ", ")

if(i * 10 % 4 != 0):
    print(n * 10)