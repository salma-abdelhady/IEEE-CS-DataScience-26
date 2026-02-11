sentence = input().split()

mx_idx = -1
mx_len = 0
for i in range(len(sentence)):
   if mx_len < len(sentence[i]):
       mx_len = len(sentence[i])
       mx_idx = i

print(f"The longest word is: {sentence[mx_idx]}")
