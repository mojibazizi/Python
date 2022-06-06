def unique_list(l):
    '''return a list of unique values form given list l'''
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x 
print(unique_list([9,9,3,4,5,4,5,2,8]))
