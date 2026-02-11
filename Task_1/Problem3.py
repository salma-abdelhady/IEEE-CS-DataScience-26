vowels = ['a', 'e', 'i', 'o', 'u']

word = input().lower()

cnt = 0
for c in word:
    if c in vowels:
        cnt += 1
        
print(f"The number of vowels is: {cnt}")