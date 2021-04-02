def search(a, n, x):
    for i in range(0,n):
        if(a[i] == x):
            return i
            
    return -1
    
a = [1,2,3,5,4]
x = 6
n = len(a)

result = search(a, n, x)
if(result == -1):
    print('not found')
    
else:
    print(f'the element is present at {result}')
    
    
    
 