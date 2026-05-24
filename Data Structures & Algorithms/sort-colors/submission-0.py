class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low,mid,high = 0,0,len(nums)-1

        while mid <=high:

            #case 0 (red)
            if nums[mid] == 0:
                nums[low],nums[mid] = nums[mid],nums[low]
                low+=1
                mid+=1
            
            #case 1 (white)
            elif nums[mid] == 1:
                mid+=1
            
            #case 2 (blue)
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -=1 #we do not move mid here as there might be one more comparision of 0,1
            

