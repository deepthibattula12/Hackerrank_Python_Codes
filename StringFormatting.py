def print_formatted(number):
    n = number  # Input the number of rows you want to print (e.g., 17)

# Calculate the width required for alignment (based on the binary representation of n)
    width = len(bin(n)[2:])

    for i in range(1, n + 1):
    # Print decimal, octal, hexadecimal (uppercase), and binary with right alignment
        print(f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {hex(i)[2:].upper().rjust(width)} {bin(i)[2:].rjust(width)}")


