# mapat(f,lst,n) applies f to the element at position n in lst. If n is negative, the position is counted from the end.
# mapat(f,lst,[i,j,...]) applies f to the part of lst at position [i,j,...]]
# mapat(f,lst,[[i1,j1,...],[i2,j2,...]]) applies f to parts of expr at several positions.

# >>> mapat(str.upper,['a','b',['c','d']],1)
# ['a', 'B', ['c', 'd']]

# >>> mapat(str.upper,['a','b',['c','d']],[2,0])
# ['a', 'b', ['C', 'd']]

# >>> mapat(str.upper,['a','b',['c','d']],[0,[2,0]])
# ['A', 'b', ['C', 'd']]

from .depth import depth
from .aslist import aslist

def mapat(f,lst,ind,*,unpack=False): 
    dep = depth(ind) 
    if dep == 0:
        mapat_mod(f,lst,[ind],unpack=unpack)
    elif dep == 1:
        mapat_mod(f,lst,ind,unpack=unpack)
    elif dep == 2:
        for i in ind:
          mapat_mod(f,lst,aslist(i),unpack=unpack)
    return lst
          
def mapat_mod(f,lst,ind,*,unpack=False):
    base = lst
    for i in ind[:-1]:
        base = base[i]
    if unpack:
        base[ind[-1]] = f(*base[ind[-1]])
    else:
        base[ind[-1]] = f(base[ind[-1]])