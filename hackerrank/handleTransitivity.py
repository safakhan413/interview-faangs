col_combi = [('a','b'), ('b','c'), ('d','e'), ('l','j'), ('c','g'),
             ('e','m'), ('m','z'), ('z','p'), ('t','k'), ('k', 'n'),
             ('j','k')]

from itertools import combinations

sets = [set(x) for x in col_combi]

stable = False
while not stable:                        # loop until no further reduction is found
    stable = True
    # iterate over pairs of distinct sets
    for s,t in combinations(sets, 2):
        if s & t:                        # do the sets intersect ?
            s |= t                       # move items from t to s
            t ^= t                       # empty t
            stable = False

    # remove empty sets
    sets = list(filter(None, sets)) # added list() for python 3

print(sets)