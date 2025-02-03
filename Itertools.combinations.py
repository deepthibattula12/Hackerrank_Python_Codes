# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

# Input the string and integer value
s, k = input().split()
k = int(k)

# Sort the string alphabetically
s = sorted(s)

# Generate and print combinations
for i in range(1, k + 1):
    for combo in combinations(s, i):
        print(''.join(combo))
