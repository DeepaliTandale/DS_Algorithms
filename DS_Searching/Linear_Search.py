def linearSearch(input,searchInput):
    for i in range(len(input)):
        if input[i] == searchInput:
            return True
    else:
        return False 


####Driver Code######
input = [12,4,23,1,98,11,21]
print(linearSearch(input,14))

#Time Complexity = O(n)
#Space Complexity = O(1)