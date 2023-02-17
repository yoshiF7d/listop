# transpose(lst) transposes the first two levels in list

# >>> transpose([['a','b','c'],['x','y','z']])
# [['a', 'b'], ['c', 'x'], ['y', 'z']]

# transpose(lst,[n1,n2,...]) transposes lst so that the k th level in lst is the nk the level in the result.

# >>> a = reshape(list(range(24)),[2,3,4])
# >>> a
# [[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]]
# >>> shape(a)
# [2, 3, 4]
# >>> b = transpose(a,[0,2,1])
# >>> b
# [[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]], [[12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23]]]
# >>> shape(b)
# [2, 4, 3]

from flatten import flatten
from shape import shape
from part import part
from reshape import reshape

def transpose(lst,axes=[1,0]):
    dim = shape(lst)
    return reshape(flatten(lst),part(dim,axes[:len(axes)]))