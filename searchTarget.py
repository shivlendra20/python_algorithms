class Solution:
        def serachTarget(self, num, target):
            
            if target in num:
                
                return num.index(target)
            
            else:
                num.append(target)
                num.sort()
                return num.index(target)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     
num = [1,3,5,9,10]
ans = Solution()
print(f'Target element is at index: {ans.serachTarget(num, 6)}')

