class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = [0]*k

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # print(sorted_items[0])

        for i in range(k):
            ans[i] = (sorted_items[i][0])
        
        return(ans)

            