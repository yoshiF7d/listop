# level(lst,lspec) gives a list of all sublists of lst on levels specified by lspec.
# lspec specifications:
#  n : levels 1 through n
#  0 : levels 1 through infinity
#  [n] : levels n only
#  [n1,n2] : levels n1 through n2

# level(lst,[-1]) gives a list of all terminal nodes in lst.
# A positive level n consists of all parts of lst specified by n indices.
# A negative level -n consists of all parts of lst with depth n.

# >>> level(['a',['b',['c','d']]],[-1])
# ['a', 'b', 'c', 'd']

# >>> level(['a',['b',['c','d']]],[2])
# ['b', ['c', 'd']]

# >>> level(['a',['b',['c','d']]],2)
# ['a', 'b', ['c', 'd'], ['b', ['c', 'd']]]

# >>> level(['a',['b',['c','d']]],0)
# ['a', 'b', 'c', 'd', ['c', 'd'], ['b', ['c', 'd']]]

from part import part
from indices import indices

def level(lst,lspec=[1]):
    return [part(lst,*i) for i in indices(lst,lspec)]


