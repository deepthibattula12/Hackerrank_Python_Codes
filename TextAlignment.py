thickness = int(input())  # Input should be an odd number for proper alignment

# Top cone
for i in range(thickness):
    print((('H' * i).rjust(thickness - 1) + 'H' + ('H' * i).ljust(thickness - 1)).center(thickness * 2))

# Top pillars
for i in range(thickness + 1):
    print(('H' * thickness).center(thickness * 2) + ('H' * thickness).center(thickness * 6))

# Middle bar
for i in range((thickness + 1) // 2):
    print(('H' * thickness * 5).center(thickness * 6))

# Bottom pillars
for i in range(thickness + 1):
    print(('H' * thickness).center(thickness * 2) + ('H' * thickness).center(thickness * 6))

# Bottom cone (right-aligned)
for i in range(thickness):
    print((('H' * (thickness - i - 1)).rjust(thickness) + 'H' + ('H' * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
