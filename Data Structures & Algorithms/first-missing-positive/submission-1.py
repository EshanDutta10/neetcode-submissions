class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        val = 1
        while val in set_nums:
            val += 1
            
        return val
        