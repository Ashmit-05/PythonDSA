import sys
from subset_sum import subset_sum
def min_subset_sum_diff(arr):
    mn = sys.maxsize
    r = sum(arr)
    s1 = list()
    for i in range(r//2 + 1):
        s = subset_sum(arr,i)
        s1.append(s)
    print(s1)
    for i in range(len(s1)):
        if s1[i] == True:
            mn = min(mn,r-2*i)
    return mn

print(min_subset_sum_diff([1,6,11,5]))

