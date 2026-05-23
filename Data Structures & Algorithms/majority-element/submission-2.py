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

        count = 0
        candidate = 0

        for num in nums:
            # 1. The fort is empty! Claim it.
            if count == 0:
                candidate = num
                count = 1
                
            # 2. A soldier from the same faction arrives. Reinforce the fort!
            elif num == candidate:
                count += 1
                
            # 3. An enemy soldier arrives. They fight one-on-one, both perish.
            else:
                count -= 1

        # Because the majority element appears more than n/2 times, 
        # its faction mathematically cannot be wiped out.
        return candidate