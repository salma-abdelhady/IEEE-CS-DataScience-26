num = input()
sz = len(num)

int_num = int(num)

sum = 0
for i in range(sz):
    d = int_num % 10
    int_num //= 10
    sum += pow(d,sz)

if sum == int(num):
    print(f"{num} is an Armstrong number")
