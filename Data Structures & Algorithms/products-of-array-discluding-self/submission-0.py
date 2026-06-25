class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        l_arr = [0] * n
        r_arr = [0] * n
        
      
        l_mul = 1
        for i in range(n):
            l_arr[i] = l_mul
            l_mul *= nums[i]
        
        
        r_mul = 1
        for i in range(n-1, -1, -1):
            r_arr[i] = r_mul
            r_mul *= nums[i]
        
        return [l_arr[i] * r_arr[i] for i in range(n)]