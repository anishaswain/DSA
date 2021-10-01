def insertion(arr): # worst-case O(n2) and average complexity of О(n) and space complexity 1
    for i in range(1,len(arr)):
        j = i-1
        anchor = arr[i]
        while j >=0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = anchor
    return arr  

arr = [3,7,5,9,0,2,4]
insertion(arr)
