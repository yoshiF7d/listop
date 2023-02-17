# reshape(lst,shape) arranges the elements of lst into a rectangular array with dimensions shape.

# >>> reshape(['a','b','c','d','e','f'],[2,3])
# [['a', 'b', 'c'], ['d', 'e', 'f']]

# >>> reshape(list(range(24)),[2,3,4])
# [[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]]

# reshape(lst,shape,padding) uses the specified padding if lst does not contain enough elements.

# >>> reshape(['a','b','c','d','e','f'],[4,3],'x')
# [['a', 'b', 'c'], ['d', 'e', 'f'], ['x', 'x', 'x'], ['x', 'x', 'x']]

import copy
from partition import partition
from map import map

def reshape(lst,shape,pad=None,level=0,*,deepcopy=False):
    if level == 0:
        size = 1
        for s in shape:
            size *= s
        
        if len(lst) < size:
            lst = lst + [pad] * (size - len(lst))
            if deepcopy:
                lst = copy.deepcopy(lst)

    elif level == len(shape):
        return lst
    
    lst = partition(lst,len(lst)//shape[level],unlist=True)

    map(lambda x : reshape(x,shape,pad,level+1,deepcopy=deepcopy),lst,inplace=True)
    return lst
