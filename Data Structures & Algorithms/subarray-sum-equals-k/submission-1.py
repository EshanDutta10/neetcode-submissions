class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # # O(n^2)
        # count = 0
        # for i in range(len(nums)):
        #     sum = 0

        #     for j in range(i,len(nums)):
        #         sum += nums[j]

        #         if sum == k:
        #             count+=1
        # return count

        # optimal approach
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1
        
        current_sum = 0
        total_subarrays = 0

        for num in nums:
            current_sum +=num

            target = current_sum - k
            # print(current_sum,target)
            if target in prefix_counts:
                total_subarrays+= prefix_counts[target]
            prefix_counts[current_sum] += 1
            
        return total_subarrays
