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

#Time Complexity = O(n(logn))
#Space Complexity = O(n)