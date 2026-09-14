# ENME 441 - Lab 2: Functions, Generators, and List Comprehension
#
# Fill in the functions below, following the assignment handout.  Each def
# line still needs its arguments -- work out from the handout what they are,
# what order they go in, and which of them have default values.  Do not change
# the function names, and submit this file without renaming it.


# Problem 1:
def between(x, a=0.0, b=0.3):
    """Return True if the value lies within the range, False if it does not."""
    return a<= x <=b


# Problem 2:
def rangef(x, step):
    """Yield successive values from 0 up to the maximum."""
    itr = 0.0
    while (itr*step)<= x:
        yield itr*step
        itr+=1


# Problem 3:
def mirror(input_list):
    """Return a new list; the list passed in must not be modified."""
    l = []
    #for i in range(len(input_list)): #must put range to allow the length of the list to be iterated over
        #l.append(input_list[i])
    for item in input_list:
        l.append(item)
    l.reverse()
    i=0
    for item in input_list:
        l.insert(i,item)
        i+=1
    return l

# #According to claude this works the same and will run more efficiently
# def mirror(input_list):
#     return input_list + input_list[::-1]
    
    
# Problem 4:
def sort_outside(input_list, a, b):
    """Return a new list with the same elements reordered."""
    l = input_list[:]#claude says it works to copy the input list to another without changing it
    l.sort(key=lambda x:not between(x,a,b)) #uses a lambda function to make an inline funct that sorts by whether its in range
    return l
    
    
#     for item in input_list:
#         if a<= item <=b:
#             l.insert(i,item)
#             i+=1
#         else:
#             l.append(item)
#     return l

# Problem 5:
def div_2_or_3():
    """Return the list described in the handout (one line of code)."""
    return [x for x in range(17) if (x % 3 ==0 or x%2==0)]


# The code below runs only when this file is executed directly (for example,
# by pressing "Run" in Thonny).  It does not run when the autograder imports
# your functions.  Leave it as-is.
if __name__ == '__main__':

    for i in rangef(5, 0.5):
        print(i, end=' ')
    print()

    alist = list(rangef(1, 0.25))
    print(alist)
    print(mirror(alist))
    print(sort_outside(mirror(alist), 0, 0.3))

    print(div_2_or_3())
