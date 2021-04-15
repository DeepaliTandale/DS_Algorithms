def insertionSort(input):
    for i in range(1,len(input)):
        current = input[i]
        j=i-1
        while j>=0 and input[j] >current:
            input[j+1] = input[j]
            j=j-1
        input[j+1] = current
    return input



####Driver Code####
input = [12,4,23,1,98,11,21]
print(insertionSort(input))

#Time Complexity = O(n**2)
#Space Complexity = O(1)