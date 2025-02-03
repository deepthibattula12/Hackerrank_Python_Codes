# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

# Input reading
n, m = map(int, input().split())
group_a = [input().strip() for _ in range(n)]
group_b = [input().strip() for _ in range(m)]

# Store indices of elements in group A using defaultdict
index_map = defaultdict(list)
for i, char in enumerate(group_a, start=1):  # 1-based indexing
    index_map[char].append(i)

# Process each element of group B
for char in group_b:
    if char in index_map:
        # Print indices as space-separated string
        print(" ".join(map(str, index_map[char])))
    else:
        # If the character from group B is not in group A
        print(-1)
