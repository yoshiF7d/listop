# intersection(lst_1,lst_2,...) gives a sorted list of the elements common to all the lst_i. 
# >>> intersection([1,1,2,3],[3,1,4],[4,1,3,3])
# [1, 3]

def intersection(*args):
    if len(args) == 0:
        return []
    else:
        result = set(args[0])
        for i in range(1, len(args)):
            result = result.intersection(set(args[i]))
        return sorted(list(result))