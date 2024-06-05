def fn(v):
    if v == 1 or v == 0:
        return 1
    
    if v % 2 == 0:
        return fn(v / 2) + 2
    else:
        return fn(v - 1) + 2
    
print(fn(7))    