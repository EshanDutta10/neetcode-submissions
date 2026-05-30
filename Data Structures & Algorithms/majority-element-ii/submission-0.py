import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = collections.Counter(nums)
        return [num for num,count in counts.items() if count>len(nums)//3]