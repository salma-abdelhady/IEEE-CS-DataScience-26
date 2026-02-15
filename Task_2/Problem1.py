n = int(input())

arr = list(map(int,input().split()))

unique_scores = sorted(set(arr), reverse=True)

max_score = max(unique_scores)

unique_scores.remove(max_score)

sec_max = max(unique_scores)

print(sec_max)