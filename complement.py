# complement(e_all,e_1,e_2,e_3,...) gives the elements in e_all that are not in any of the e_i. 

# >>> omplement(['a','b','c','d','e'],['a', 'c'], ['d'])
# ['b','e']

def complement(e_all, *args):
    e_all = set(e_all)
    for e in args:
        e_all -= set(e)
    return list(e_all)
