n = int(input())

records = []
grades = []

for _ in range(n):
    name = input()
    grade = float(input())
    
    records.append([name, grade])
    
    grades.append(grade)
    
    grades = sorted(set(grades))

second_lowest = grades[1]

output = []
for record in records:
    if record[1] == second_lowest:
        output.append(record[0])

output.sort()

for i in range(len(output)):
    print(output[i])