

from bisect import bisect_left,bisect_right

class Solution:
    def searchRange(self, num, target):
        
        l = bisect_left(num, target)
        r = bisect_right(num, target)
        
        if l<r:
            return (l,r-1)
        else:
            return (-1,-1)
       # return (bisect_left(nums,target),bisect_right(nums,target)-1) if bisect_left(nums,target)<bisect_right(nums,target) else (-1,-1)
        
        
        
        
        
num = [1,3,5,7,9,11]
a = Solution()
print(f'The First and Last postion of the target element is: \n{a.searchRange(num, 7)}')
