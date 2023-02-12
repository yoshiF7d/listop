# part(lst,i) gives the i th part of lst.
# part(lst,i,j,...) is equivalent to lst[i][j]....
# part(lst,[i1,i2,...]) gives a list of the parts i1, i2, ... of lst.

def part(lst,*ind):
    if isinstance(ind[0],list): 
        return [lst[i] for i in ind[0]]
    else:
        res = lst
        for i in ind:
            res = res[i]
        return res