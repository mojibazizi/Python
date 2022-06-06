def max_and_min(lst):
    """Returns max and min of given list."""

    #Returns tuple containing max and min of list 
    return (max(lst), min(lst))

def main():
    list1 = [25, -9, -34, 18]
    maxandmin = max_and_min(list1)
    #lets check the type
    print(type(maxandmin))
    #get max from tuple
    max = maxandmin[0]
    #get min from tuple
    min = maxandmin[1]
    print(max, min)
    #another way to do this 
    #double variable assignment, to get tuple values directly
    maxv2, minv2 = max_and_min(list1)
    print(maxv2, minv2)
    

#calling the main function
if __name__ == '__main__':
    main()