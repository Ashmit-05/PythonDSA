def bubbleSort(arr) :
    for i in range(0,len(arr)) :
        for j in range(0,len(arr)-i-1) :
            if arr[j] > arr[j+1] :
                arr[j],arr[j+1] = arr[j+1],arr[j]
nums = [1,5,3,2,6,2,4,9]
bubbleSort(nums)
print(nums)
