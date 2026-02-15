filename = 'Task_2/simple_test.txt'

sat_words = []

with open(filename, 'r') as file:
    for line in file:
        words = line.split()
        
        for word in words:
            clean_word = ''.join(char for char in word if char.isalnum())

            if len(clean_word) > 5:
                sat_words.append(clean_word)

unique_words = set(sat_words)
for word in unique_words:
    print(word)