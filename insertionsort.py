def insertionsort(a):
    
    for i in range(1, len(a)):
        
        key = a[i]
        j = i-1
        
        while j>=0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
            
        a[j+1] = key
        
        
a = [2,6,5,4,8,7]

insertionsort(a)
print(f'The sorted array is: {a}')
        