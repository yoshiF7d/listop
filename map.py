# map(f,lst) applies f to each element on the first level in lst.
# map(f,lst,lspec) applies f to parts of lst specified by lspec.

# lspec specifications:
#  n : levels 1 through n
#  0 : levels 1 through infinity
#  [n] : levels n only
#  [n1,n2] : levels n1 through n2

# level(lst,[-1]) gives a list of all terminal nodes in lst.
# A positive level n consists of all parts of lst specified by n indices.
# A negative level -n consists of all parts of lst with depth n.

# The default value for lspec in map is [1].
# map always constructs a complete new list.

# >>> map(str.upper,['a','b','c'])
# ['A', 'B', 'C']

# >>> map(str.upper,['a',['b','c']],[2])
# ['a', ['B', 'C']]

# >>> map(str.upper,['a','b',['b','c'],'d'],[-1,1])
# ['A', 'B', ['b', 'c'], 'D']

import copy
from mapat import mapat_mod
from indices import indices

def map(f,lst,lspec=[1],*,unpack=False):
    lst = copy.deepcopy(lst)
    for i in indices(lst,lspec):
        mapat_mod(f,lst,i,unpack=unpack)
    return lst