# Time complexity of Merge Sort is O(n*Log n) => log n for sort and n for merge
def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
#     print("left ======>:",left)
#     print("right =====> :",right)
    
    mergeSort(left)
    mergeSort(right)   

#     print("arr :",arr)
    
    sort_two_sorted_list(left,right,arr)
    print(arr)

def sort_two_sorted_list(a,b,arr):
#     shorted_list = []
    la = len(a) #3
    lb = len(b) #4
    
    i = j = k = 0
    while i < la and j < lb:
        if a[i] < b[j]:
            arr[k] = a[i]
            i+=1
            k+=1
#             shorted_list.append(a[i])
#             i+=1
        else:
            arr[k] = b[j]
            j+=1
            k+=1
#             shorted_list.append(b[j])
#             j+=1
    while i<la:
        arr[k] = a[i]
        i+=1
        k+=1
#         shorted_list.append(a[i])
#         i+=1
    while j<lb:
        arr[k] = b[j]
        j+=1
        k+=1
#         shorted_list.append(b[j])
#         j+=1
#     print(arr)
#     return shorted_list

arr = [5,4,3,2,1]
mergeSort(arr)
