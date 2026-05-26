class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # # DIVISION ALLOWED
        # product_without_zero = 1
        # zero_count = 0
        # output = []

        # for num in nums:
        #     if num == 0:
        #         zero_count+=1
        #     else:
        #         product_without_zero *= num
        
        # if zero_count >=2:
        #     return [0]*len(nums)
        
        # for num in nums:
        #     if zero_count == 1:
        #         if num == 0:
        #             output.append(product_without_zero)
        #         else:
        #             output.append(0)
        #     else:
        #         output.append(product_without_zero//num)
        
        # return output

        # # DIVISION NOT ALLOWED
        n = len(nums)
        output = [1]*n

        left_product,right_product = 1,1

        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        
        for j in range(n-1,-1,-1):
            output[j] *= right_product
            right_product *= nums[j]
        
        return output
