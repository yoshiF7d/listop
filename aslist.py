# This function checks if the input is a list, if it is then it returns it as it is, 
# otherwise it returns the input as a single element list.

def aslist(a):
    if isinstance(a,list):
        return a
    else:
        return [a]