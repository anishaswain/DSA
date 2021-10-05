def selection_sort(arr): # worst-case O(n2) and average complexity of О(n2) and space complexity 1 
    for i in range(0,len(arr)-1):
        minimum = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minimum]:
                minimum = j
        if i != minimum:    
            arr[i],arr[minimum] = arr[minimum],arr[i]
        print(arr)
    return arr

arr = [3,7,5,9,0,2,4]
selection_sort(arr)
