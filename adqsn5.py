from functools import reduce
def maxterm(n,r):
    if (n>=r):
        return n
    else:
        return r
l=[1,2,3,4]
print(reduce(maxterm,l))