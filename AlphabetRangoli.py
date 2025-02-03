def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Generate the top half and the middle line
    for i in range(size):
        # Characters for the current row
        chars = "-".join(alphabet[size - 1:size - 1 - i:-1] + alphabet[size - 1 - i:size])
        # Center the row with dashes
        print(chars.center(4 * size - 3, '-'))
    
    # Generate the bottom half
    for i in range(size - 2, -1, -1):
        # Characters for the current row
        chars = "-".join(alphabet[size - 1:size - 1 - i:-1] + alphabet[size - 1 - i:size])
        # Center the row with dashes
        print(chars.center(4 * size - 3, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
