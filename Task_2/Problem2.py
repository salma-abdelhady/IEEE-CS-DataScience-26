n = int(input())  

arr = []

for _ in range(n):
    command = input().strip().split()
    input_op = command[0].lower()

    if input_op == 'insert':
        i = int(command[1])
        e = int(command[2])
        arr.insert(i, e)
    
    elif input_op == 'print':
        print(arr)
    
    elif input_op == 'remove':
        e = int(command[1])
        arr.remove(e)
    
    elif input_op == 'append':
        e = int(command[1])
        arr.append(e)
        
    elif input_op == 'sort':
        arr.sort()
    
    elif input_op == 'pop':
        arr.pop()
    
    elif input_op == 'reverse':
        arr.reverse()
