

# Complete the solve function below.
def solve(name):
    h1=[]
    word_list = re.findall(r'\S+|\s+', name)
    for i in word_list:
        h1.append(i.capitalize())
    return ''.join(h1)

