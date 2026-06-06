class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # # space is O(n) due to the new set
        # set_nums = set(nums)
        # val = 1
        # while val in set_nums:
        #     val += 1
            
        # return val

        # optimal 
        n = len(nums)

        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] -1
                nums[target_idx],nums[i] = nums[i],nums[target_idx]
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        return n+1
        