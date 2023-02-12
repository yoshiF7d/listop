# union(lst_1,lst_2,...) gives a sorted list of all the distinct elements that appear in any of the lst_i.
# union(lst) gives a sorted version of a list, in which all duplicated elements have been dropped.

from flatten import flatten
def union(*lst):
    return sorted(list(set(flatten(lst))))