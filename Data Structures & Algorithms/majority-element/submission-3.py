class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # current,max_count = 0,0

        # nums.sort()
        # for i in range (1,len(nums)):
        #     if nums[i-1] == nums[i]:
        #         current+=1
        #     else:
        #         current = 0
        #         max_count = max(max_count,current)
        #     max_count = max(max_count,current)
        # return nums[max_count]

        candidate,count = 0,0

        for num in nums:
            if count ==0:
                candidate = num
                count=1
            
            if candidate ==num:
                count+=1
            
            else:
                count-=1
        return candidate