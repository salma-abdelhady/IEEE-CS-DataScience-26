import random
import string 

chars = string.digits + string.ascii_letters

password = ''
for i in range(8):
    password += random.choice(chars)

print(password)