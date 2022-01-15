arr = [1, 0, 2, 3, 0, 4, 5, 0]

#[1, 0, 2, 3, 0, 4, 5, 0]  input
#[1,0,0,2,3,0,0,4]  output

#

"""

# Python3 program to swap elements
# at given positions
 
# Swap function
def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Driver function
List = [23, 65, 19, 90]
pos1, pos2  = 1, 3
 
print(swapPositions(List, pos1-1, pos2-1))

"""


def mysteryFunction(arr):
    tempArr = []
    tempArr+=arr

    for i in range(len(arr)):
        if tempArr[i] == 0:
            for x in range(-1, -len(arr) + i, -1):
                arr[x] = arr[x - 1]
                tempArr[i] = 1
                tempArr[x] = tempArr[x - 1]




mysteryFunction([1, 0, 2, 3, 0, 4, 5, 0])
print(arr)
