arrayToSort = input("array: ")


def bubbleSort(array):
    for i in range(len(array)):
        for j in range((len(array)-1 - i)):
            n = array[j + 1]
            p = array[j]
            if p > n:
                temp = array[j]
                array[j] = array[j + 1]
                array[j+1] = temp
    print(array)


bubbleSort(arrayToSort)