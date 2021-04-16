def binarySearch(input, searchInput):
    input.sort()
    first = 0
    last = len(input)-1
    print(input)
    while first <=last:
        mid = (first+last)//2
        #print(mid)
        if input[mid]==searchInput:
            return mid,searchInput
        elif searchInput > input[mid]:
            first = mid+1
        else:
            last =mid-1
    if first>last:
        return None


####Driver Code######
input = [12,4,23,1,98,11,21]
print(binarySearch(input,1))


#Time Complexity = O(log n)
#Space Complexity = O(1)