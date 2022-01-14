arr = [1, 0, 2, 3, 0, 4, 5, 0]


#[1,0,0,2,3,0,0,4]
tempArr = []

tempArr+=arr


for i in range(len(arr)):
    if tempArr[i] == 0:
        for x in range(-1, -len(arr) + i, -1):
            arr[x] = arr[x - 1]
            tempArr[i] = 1
            tempArr[x] = tempArr[x - 1]


print(arr)
