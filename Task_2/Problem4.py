n = int(input())

students = {}

for _ in range(n):
    record = input().split()
    
    grades = [float(record[1]), float(record[2]), float(record[3])]
    
    students[record[0]] = grades
    
asked = input()

total = sum(students[asked])

avg = total / len(students[asked])

print(f'{avg:.2f}')
    