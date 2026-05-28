class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # # O(n log n)

        # # Edge case: If the array is empty, the longest sequence is 0
        # if not nums:
        #     return 0
        
        # #sorting 
        # nums.sort()

        # cur = 1
        # max_cur = 1

        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]: #same ele
        #         continue
            
        #     elif nums[i] == (nums[i-1] + 1):
        #         cur +=1
            
        #     else:
        #         max_cur = max(max_cur,cur)
        #         cur = 1
        
        # return max(max_cur,cur)

        # O(n)

        num_set = set(nums)
        longest_streak = 0
        current_streak = 0
        current = 0

        for num in num_set:
            if (num-1) not in num_set:
                current_num = num
                current_streak = 1

                while (current_num+1) in num_set:
                    current_num+=1
                    current_streak +=1
                longest_streak = max(current_streak,longest_streak)
        return longest_streak
