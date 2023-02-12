# flatten(lst) flattens out nested lists.
# flatten(lst,n) flattens to level n.

def flatten(lst,level=-1):
    if level == 0:
        return lst
    else:
        flat_list =[]
        for element in lst:
            if isinstance(element,list):
                flat_list.extend(flatten(element,level-1))
            else:
                flat_list.append(element)
        
        return flat_list