# indices(lst,lspec) gives a list of all indices of sublists of lst on levels specified by lspec.
# lspec specifications:
#  n : levels 1 through n
#  0 : levels 1 through infinity
#  [n] : levels n only
#  [n1,n2] : levels n1 through n2

# indices(lst,[-1]) gives a list of all terminal nodes in lst.
# A positive level n consists of all parts of lst specified by n indices.
# A negative level -n consists of all parts of lst with depth n.

# >>> indices(['a',['b',['c','d']]],[-1])
# [[0], [1, 0], [1, 1, 0], [1, 1, 1]]

# >>> indices(['a',['b',['c','d']]],[2])
# [[1, 0], [1, 1]]

# >>> indices(['a',['b',['c','d']]],2)
# [[0], [1, 0], [1, 1], [1]]

# >>> indices(['a',['b',['c','d']]],0)
# [[0], [1, 0], [1, 1, 0], [1, 1, 1], [1, 1], [1]]

from .aslist import aslist
from .depth import depth

def indices(lst,lspec=[1]):
    if isinstance(lspec,int):
        if lspec == 0:
            lspec = [1,depth(lst)]
        else:
            lspec = [1,lspec]
    if len(lspec) == 1:
        lspec = [lspec[0],lspec[0]]
    return indices_mod(lst,lspec,lev=0,ind=[])

def indices_mod(lst,lspec,lev,ind):
    res = []
    dep = depth(lst)
    l1,l2 = lspec
    
    if isinstance(lst,list):
        for i,item in enumerate(lst):
            res.extend(indices_mod(item,lspec,lev+1,ind+[i]))
    
    if l1 < 0:
        l1 += lev + dep + 1
    if l2 < 0:
        l2 += lev + dep + 1
    
    if l1 <= lev and lev <= l2:
        res.append(ind)
    
    return res

#ef indices_all(lst):
#    res = []
#    if isinstance(lst,list):
#        for i,item in enumerate(lst):
#            res.extend(indices_thread(i,indices_all(item)))
#    return res

#def indices_thread(a,lst):
#    if lst:
#        return [[a] + aslist(b) for b in lst]
#    else:
#        return [a]