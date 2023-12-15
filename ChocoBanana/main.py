import itertools

x = list(itertools.product([0,1], repeat=12))

print(len(x))