# tally(lst) tallies the elements in lst, listing all distinct elements together with their multiplicities.

# >>> tally(['a','a','b','a','c','b','a'])
# [['a', 4], ['b', 2], ['c', 1]]

def tally(lst):
    tally = {}
    for element in lst:
        if element in tally:
            tally[element] += 1
        else:
            tally[element] = 1
    
    return [[key,tally[key]] for key in tally]