class Solution:
    def merge (self,left: List[int], right: List[int]) -> List[int]:
            i,j=0,0
            merged = []
            while i<len(left) and j<len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i+=1
                else:
                    merged.append(right[j]) 
                    j+=1         
            while i<len(left):
                merged.append(left[i])
                i+=1
            while j<len(right):
                merged.append(right[j])
                j+=1
            return merged

    def sortArray(self, nums: List[int]) -> List[int]:

        #base case: only one element
        if len(nums)<=1:
            return nums
        
        #dividing the array
        middle = len(nums)//2
        left = nums[:middle]
        right = nums[middle:]

        #sort the sub arrays by calling function recursively
        sorted_left = self.sortArray(left)
        sorted_right = self.sortArray(right)

        return self.merge(sorted_left,sorted_right)
        
        
        

        