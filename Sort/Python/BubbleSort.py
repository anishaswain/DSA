def bubble(arr): # worst-case and average complexity of О(n2) and space complexity 1
    for j in range(0,len(arr)-1):
        swap = False
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swap = True
        if not swap:
            break
    return arr
arr = [3,7,5,9,0,2,4]
bubble(arr)
