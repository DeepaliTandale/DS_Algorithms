def bubbleSort(input):
    for i in range(len(input)-1,0,-1):
        for j in range(i):
            if input[i] < input[j]:
                temp = input[i]
                input[i] = input[j]
                input[j] = temp
    return input

####Driver Code####
input = [12,4,23,1,98,11,21]
print(bubbleSort(input))

#Time Complexity = O(n**2) 
#Space Complexity = O(1)