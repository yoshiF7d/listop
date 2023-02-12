# gather(lst) gathers the elements of lst into sublists of identical elements.

# >>> gather(['a', 'b', 'a', 'd', 'b'])
# [['a', 'a'], ['b', 'b'], ['d']]

def gather(lst):
    result = []
    for element in lst:
        found = False
        for sublist in result:
            if sublist[0] == element:
                sublist.append(element)
                found = True
                break
        if not found:
            result.append([element])
    return result