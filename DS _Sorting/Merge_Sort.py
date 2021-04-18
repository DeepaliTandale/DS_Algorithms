def mergeSort(input):
    if len(input) > 1:
        midPt = len(input)//2
        leftArray = input[:midPt]
        rightArray = input[midPt:]
        #print(leftArray)
        #print(rightArray)

        ########RECURSIVE CALL ON DATASETS########
        mergeSort(leftArray)
        mergeSort(rightArray)

        i,j,k=0,0,0

        while i<len(leftArray) and j<len(rightArray):
            if leftArray[i] < rightArray[j]:
                input[k] = leftArray[i]
                i+=1
            else:
                input[k] = rightArray[j]
                j+=1
            k+=1

        while i<len(leftArray):
            input[k] = leftArray[i]
            i+=1
            k+=1

        while j<len(rightArray):
            input[k] = rightArray[j]
            j+=1
            k+=1

    return input

####Driver Code####
input = [12,4,23,1,98,11,21,45,16,7]
print(mergeSort(input))


"""
Time Complexity = O(n(logn))
Space Complexity = O(n)

mergesort calls itself on the order of log(n) times.The extra space comes from the merge operation.
Most implementations of merge use an additional array with length equal to the length of the merged result, 
since in-place merges are very complicated. 
In other words, to merge two sorted arrays of length n/2, most merges will use an auxiliary array of length n.
The final step of mergesort does exactly this merge, hence the O(n) space requirement.

The key difference between the quick and merge sort lies in the space requirement of the operation performed at each recursive step.
The partition step used in quicksort is an IN-PLACE operation,
while merging usually requires an auxiliary/extra/helper/additional array.
"""