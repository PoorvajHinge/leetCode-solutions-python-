class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3:
            return -1
        else:
            nums.sort()
            return nums[1]
        
        