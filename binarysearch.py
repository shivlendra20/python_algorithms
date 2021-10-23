def binarysearch(a, l, r, x):
    if l<=r:
        mid = l + (r-l) // 2
        
        if a[mid] == x:
            return mid
        elif a[mid] > x:
            return binarysearch(a, l, mid-1, x)
        else:
            return binarysearch(a, mid+1, r, x)
            
    else:
        return -1
    
    
a = [5,4,9,3,6,8,7,10,12,15,23,43,23,11,120]
x = 4

result = binarysearch(a, 0, len(a)-1, x)

if result == -1:
    print('not found')
else:
    print(f'the element is at index {result}')
