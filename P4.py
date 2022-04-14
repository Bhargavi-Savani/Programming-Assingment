from itertools import combinations
num = [int(n) for n in input().split()] 
k = int(input()) 
count = 0 
for i in range(1, len(num)+1): 
 for c in combinations(num, i): 
    if sum(c) == k: 
        count += 1
print(count)