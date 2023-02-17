# length(lst) gives the number of elements in lst

def length(lst):
    if isinstance(lst,list):
        return len(lst)
    else:
        return 0