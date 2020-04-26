

class Solution:

    # Uses O(n) mem to build options list
    def solution1(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        max_amounts = []
        max_amounts.append(nums[0])
        max_amounts.append(nums[1])

        # TODO - can do this without array, just hard code the 3 variables
        for i in range(2, len(nums)):
            print(max_amounts)
            if i == 2:
                max_amounts.append(nums[i] + nums[i-2])
                continue

            print('i: {}, nums[i]: {}'.format(i, nums[i]))
            two_back = max_amounts[i-2] + nums[i]
            three_back = max_amounts[i-3] + nums[i]
            print("comparing {} with {}".format(two_back, three_back))
            max_amounts.append(max(two_back, three_back))

        print('max_amounts: {}'.format(max_amounts))
        return max(max_amounts[-1], max_amounts[-2])

    # Uses O(1) mem, no list
    def solution2(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        three_back, two_back, one_back = nums[0], nums[1], nums[2] + nums[0]
        
        for i in range(2, len(nums)):
            # Special case, already calculated
            if i == 2:
                continue

            new_max = max(nums[i] + three_back, nums[i] + two_back)

            three_back = two_back
            two_back = one_back
            one_back = new_max
        
        return max(two_back, one_back)
        

    def rob(self, nums):
        return self.solution2(nums)
            
            
s = Solution()
#print(s.rob([1,2,3,4]))
print(s.rob([1,2,3,1]))
print(s.rob([2,7,9,3,1]))
