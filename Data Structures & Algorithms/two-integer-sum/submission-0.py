class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = 0
        for i in range(len(nums)):
            temp = nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] + temp == target:
                    return [i,j]
                
        