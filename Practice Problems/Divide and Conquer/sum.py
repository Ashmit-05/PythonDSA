def sum(arr:list) :
    if len(arr) == 1 :
        return 1
    else :
        arr.pop()
        return 1+sum(arr)

print("length of array : ",sum([1,23,23,44]))
