class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dicts = {}

        for i,n in enumerate(nums):
            target_temp = target - n
            if target_temp in dicts:
                return [dicts[target_temp],i]
            dicts[n] = i