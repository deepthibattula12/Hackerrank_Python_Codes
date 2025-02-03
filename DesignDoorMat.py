# Input values for rows and columns
#n=9
#m=27
n=input().split()
# Top half of the pattern
for i in range(int(n[0]) // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(int(n[1]), '-'))

# Middle line with "WELCOME"
print("WELCOME".center(int(n[1]), '-'))

# Bottom half of the pattern
for i in range(int(n[0])// 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(int(n[1]), '-'))
