n = int(input())

for _ in range(n):    
    try:
        a, b = map(int,input().split())
        print(a // b)
        
    except ZeroDivisionError as e:
        print(f"Error Code: {e}")
    
    except ValueError as e:
        print(f"Error Code: {e}")