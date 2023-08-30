def local_variable():
    global a
    a=1
    b=2
    c=3
    
print(local_variable.__code__.co_nlocals)