import itertools as it

def print_pairs(no):
    nos=range(1,no+1)
    combos=[(it.combinations(nos,pairs)) for pairs in nos]
    print([pair for combo in combos for pair in combo if sum(pair) == no])

print_pairs(8)
