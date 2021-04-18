def quickSort(input,first,last):
    if first <last:
        pivotPt = quickSortWrapper(input,first,last)
        quickSort(input,first,pivotPt-1)
        quickSort(input,pivotPt+1,last)


def quickSortWrapper(input,first,last):
    pivotVal = input[first]
    lower = first+1
    upper = last
    done = False
    while not done:
        while lower <= upper and input[lower] <= pivotVal:
            #print("0 lower = ",lower,"upper = ",upper)
            lower+=1
        while upper >=lower and input[upper] >= pivotVal:
            #print("1 lower = ",lower,"upper = ",upper)
            upper -=1

        if lower > upper:
            #print("2 lower = ",lower,"upper = ",upper)
            done = True
        else:
           
            temp = input[lower]
            input[lower] = input[upper]
            input[upper] = temp
            #print("3 lower = ",lower,"upper = ",upper)
            #print(input)

    temp = input[first]
    input[first] = input[upper]
    input[upper] = temp
    #print("4 lower = ",lower,"upper = ",upper)
    #print(input)
    return upper



####Driver Code####
input = [12,4,23,1,98,3]
#print(input[0],input)
quickSort(input,0,len(input)-1)
print(input)

"""
Time Complexity = O(n(log n))
#Space Complexity = O(log n)

Quicksort calls itself on the order of log(n) times (in the average case, worst case number of calls is O(n)),
at each recursive call a new stack frame of constant size must be allocated.
Hence the O(log(n)) space complexity.
"""