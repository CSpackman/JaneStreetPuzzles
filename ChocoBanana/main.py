import itertools

x = list(itertools.product([0,1], repeat=49))

print(len(x))