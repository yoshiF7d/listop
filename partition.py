# partition(lst,n) partitions lst into nonoverlapping sublists of length n.
# >>> partition(['a','b','c','d','e'],2)
# [['a', 'b'], ['c', 'd']]

#partition(lst,n,tail=True) partitions into sublists of length up to n, allowing the final sublist to be shorter.
# >>> partition(['a','b','c','d','e'],2,tail=True)
# [['a', 'b'], ['c', 'd'], ['e']]

# partition(lst,n,d) generates sublists with offset d. 
# >>> partition(['a','b','c','d','e','f','g'],3,1)
# [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e'], ['d', 'e', 'f'], ['e', 'f', 'g']]

def partition(lst,n,d=None,*,tail=False,unlist=False):
    if d is None:
        d = n
    
    if unlist and n==1:
        rtn = [lst[i] for i in range(0,len(lst),d)]
    else:
        rtn = [lst[i:i+n] for i in range(0,len(lst),d)]
    
    if tail:
        return rtn
    else:
        return rtn[:(len(lst)-n)//d+1]