def selectionSort(input):
    for i in range(0,len(input)):
        minIndex = i
        for j in range(i+1,len(input)):
            if input[j] <=input[minIndex]:
                minIndex =j
        # temp = input[i]
        # input[i] = input[minIndex]
        # input[minIndex] = temp
        input[i],input[minIndex] = input[minIndex],input[i]
    return input


####Driver Code####
input = [12,4,23,1,98,11,21]
print(selectionSort(input))

#Time Complexity = O(n**2)
#Space Complexity = O(1)