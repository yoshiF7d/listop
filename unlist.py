# unlist(e) returns e if it is not a list with a single element. 
# If the input is a list with a single element, it returns that single element. 

def unlist(a):
    if isinstance(a,list):
        if len(a) == 1:
            return a[0]    
    return a