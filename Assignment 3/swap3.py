#Python program to interchange ﬁrst and last elements in a list
# Python3 program to swap ﬁrst  and last element of a list 
# Swap function
def swapList(list): 
# Storing the ﬁrst and last element
# as a pair in a tuple variable get
    get = list[-1], list[0] 
# unpacking those elements
    list[0], list[-1] = get 
    return list
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList)) 
