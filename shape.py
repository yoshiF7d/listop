# dimensions(lst) gives a list of the dimensions of lst.
from .length import length

def shape(lst,dim=None):
    if dim is None:
        dim = [] # https://web.archive.org/web/20200221224620id_/http://effbot.org/zone/default-values.htm
    
    size = length(lst[0])
    for l in lst[1:]:
        if size != length(l):
            size=0
            break

    dim.append(len(lst))
    if size == 0:
        return dim
    return shape(lst[0],dim)