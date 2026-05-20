class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        # if len(nums)!=len(seen):
        #     return True
        # return False

        # for big arrays, this is a better solution
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
            