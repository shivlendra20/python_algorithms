def partition(a, lb, ub):
    pivot = a[lb]
    start = lb
    end = ub
    
    while start < end:
        while a[start] <= pivot:
            start += 1
        while a[end] > pivot:
            end -= 1
        if start < end:
            a[start], a[end] = a[end], a[start]
            
    a[lb], a[end] = a[end], a[lb]
    return end
    
            
def quicksort(a, lb, ub):
    if lb < ub:
        
        loc = partition(a, lb, ub)
        quicksort(a, lb, loc-1)
        quicksort(a, loc+1, ub)
        
a = [2,6,7,9,5,4]
n = len(a)
quicksort(a, 0, n)
print(a)

        