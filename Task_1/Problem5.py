n = int(input())

fib = [0,1]

if n == 1:
    print(0)

elif n == 2:
    print("0, 1")

else:
    print("0, 1", end=", ")
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
        if i != n - 1: 
            print(fib[i], end=", ")
        else: 
            print(fib[i])
