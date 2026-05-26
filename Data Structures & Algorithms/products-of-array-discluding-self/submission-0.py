class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #if division is allowed
        product_without_zero = 1
        zero_count = 0
        output = []

        for num in nums:
            if num == 0 :
                zero_count +=1
            else:
                product_without_zero *= num
        
        if zero_count >=2:
            return [0]*len(nums)
        
        else:
            for num in nums:
                if zero_count ==1:
                    if num == 0:
                        output.append(product_without_zero)
                    else:
                        output.append(0)
                else:
                    output.append(product_without_zero//num)
        return output
