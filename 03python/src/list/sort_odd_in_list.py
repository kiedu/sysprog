'''
Sort the odd
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]   = >  [1, 7]
[5, 8, 6, 3, 4]   = >  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]   = >  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
'''


def sort_array(source_array):
    a = list(source_array)
    b = [None] * len(a)
    c = []
    for i in range(0,len(a),1):
        if int(a[i])%2 =  = 0:
            b[i] = a[i]
        else:
            c.append(a[i])
    c.sort()
    for j in range(0,len(b),1):
        if b[j]! = None:
            c.insert(j,b[j])
    return c
