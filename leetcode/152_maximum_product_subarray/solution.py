from functools import reduce
from math import inf

class Solution:
    # Ignore zeros for now
    def max_product_no_zeros(self, nums):
        if len(nums) == 1:
            return nums[0]

        first_neg_idx, last_neg_idx = -1, -1
        num_negs = 0
        
        total_product = None

        for i in range(len(nums)):
            # Handle negative number
            if nums[i] < 0:
                # First negative number
                if num_negs == 0:
                    first_neg_idx = i

                num_negs += 1
                last_neg_idx = i

            if i == 0:
                total_product = nums[i]
            else:
                total_product = total_product * nums[i]

        # Now we have product of entire thing...
        # If product is positive, return it (means we had even # negatives)
        # If prod is negative, create subarray by removing beginning or end
        if total_product > 0:
            return total_product
        else:
            product_up_thru_first_neg = reduce(lambda x,y : x * y, nums[0 : first_neg_idx + 1])
            product_up_after_incl_last_neg = reduce(lambda x,y : x * y, nums[last_neg_idx:])

            return max(total_product / product_up_thru_first_neg, total_product / product_up_after_incl_last_neg)

    def maxProduct(self, nums):
        # find locations of zeros and get product of left and right
        for i in range(len(nums)):
            if nums[i] == 0:
                left_prod = self.max_product_no_zeros(nums[0:i]) if i > 0 else 0

                right_prod = self.max_product_no_zeros(nums[i+1:]) if i < len(nums) - 1 else 0

                return max(left_prod, 0, right_prod)

        return self.max_product_no_zeros(nums)

s = Solution()

# Tests without zeros
print(s.maxProduct([1, 2, 3, 4, 5]))  # Easy test
print(s.maxProduct([1, -1, 2, 3, 4, -1, 5]))  # same as above, with negatives
print(s.maxProduct([5, -1, 4]))
print(s.maxProduct([4, -1, 5]))
print(s.maxProduct([1, 2, 3, 4, -1, 5]))  # Take left side
print(s.maxProduct([1, 2, 3, 0, 4, -1, 5]))  # left of zero
print(s.maxProduct([1, 2, 3, 0, 2, 4, -1, 5]))  # 8
print(s.maxProduct([1, 2, 3, 0, 2, 4, -1, 5, 2]))  # 10
print(s.maxProduct([1, 2, 3, 0, 2, 4, -1, 5, -2, -1]))  # right of zero
