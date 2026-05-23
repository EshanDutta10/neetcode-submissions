class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        complement = 0

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in check:
                return [check[complement], i]
            
            check[nums[i]] = i
                
        