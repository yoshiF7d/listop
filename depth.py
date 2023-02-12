# depth(lst) gives the maximum number of indices needed to specify any part of lst

def depth(lst):
    dep = -1
    if isinstance(lst,list):
        for item in lst:
            dep = max(dep,depth(item))
    
    return dep + 1