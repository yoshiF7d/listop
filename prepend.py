# prepend(lst,x) gives lst with x prepended.

# >>> prepend(['a','b','c','d'],'x')
# ['x','a','b','c','d']

def prepend(lst,x):
    return [x] + lst