def bubblesort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    
a = [2,4,5,9,7,6]
bubblesort(a)

print(f'Sorted array is : {a}')