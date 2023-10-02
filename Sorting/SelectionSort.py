def selectionSort(arr) :
    for i in range(len(arr)) :
        min_index = i
        for j in range(i+1,len(arr)) :
            if arr[j] < arr[min_index] : 
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

arr = [5,2,4,5,6,3,9,7,1]
selectionSort(arr)
print(arr)
