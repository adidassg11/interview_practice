class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return self.maxSA2(nums)
        #return self.max_sa_kadanes(nums)
        return self.max_sa_recursive(nums)
        
    def maxSA1(self, nums):
        maxes_list = []
        running_total = 0
        for i, val in enumerate(nums):
            running_total += val
            maxes_list.append(running_total)

    def maxSA2(self, nums):
        running_total = 0
        max_range_start = 0
        max_range_end = 0

        for i, val in enumerate(nums):
            running_total += val
            if running_total >= 0:
                max_range_end = i
                print(locals())
                continue
            running_total = 0
            max_range_start = i
            max_range_end = i
            print(locals())

        print(locals())
        print()

    def max_sa_kadanes(self, nums):
        ans_sa_value = nums[0]
        ans_sa_start = 0
        ans_sa_end = 0

        if not len(nums):
            return

        cur_sa_value = 0
        cur_sa_start = 0
        cur_sa_end = 0

        for i, val in enumerate(nums):
            cur_sa_value += val
            cur_sa_end = i

            # found new max subarray
            if cur_sa_value > ans_sa_value:
                ans_sa_value = cur_sa_value
                ans_sa_start = cur_sa_start
                ans_sa_end = cur_sa_end

            # didn't find new max, but keep building local subarray
            print(locals())

            # local max subarray ends, start over
            if cur_sa_value < 0:
                cur_sa_value = 0
                cur_sa_start = i+1
                cur_sa_end = i+1
                print(locals())
                continue

        return ans_sa_value

    '''
    [1] len = 1
    [1,2] len = 2
    [1,2,3] len = 3
    [1,2,3,4] len = 4
    [1,2,3,4,5] len = 5
    '''

    # TODO - almost there in terms of logic
    # TODO - decide whether joining means index is equal or one apart
    def max_sa_recursive_helper(self, nums, start_idx, end_idx):
    #def max_sa_recursive_helper(self, nums):
        if start_idx == end_idx:
        #if len(nums) == 1:
            return (nums[0], 0, 0)

        # left side 
        #(left_max, left_max_start, left_max_end) = self.max_sa_recursive_helper(nums[:(len(nums)-1)//2])
        (left_max, left_max_start, left_max_end) = self.max_sa_recursive_helper(nums, start_idx, end_idx//2)
        # right side
        (right_max, right_max_start, right_max_end) = self.max_sa_recursive_helper(nums[len(nums)//2:])

        print("evaluating {} with {}".format((nums[left_max_start:left_max_end], nums[right_max_start:right_max_end])))

        # can merge?
        if left_max_end == right_max_start:
            # see if merging makes sense
            if left_max > 0 and right_max > 0:
                merged_max = left_max + right_max
                merged_start = left_max_start
                merged_end = right_max_end
                return (merged_max, merged_start, merged_end)

        if left_max > right_max:
            return (left_max, left_max_start, left_max_end)
        return (right_max, right_max_start, right_max_end)


    def max_sa_recursive(self, nums):
        import pdb; pdb.set_trace()
        # left side 
        #(left_max, left_max_start, left_max_end) = self.max_sa_recursive_helper(nums[:(len(nums)-1)//2])
        (left_max, left_max_start, left_max_end) = self.max_sa_recursive_helper(nums, 0, (len(nums)-1)//2)

        # right side
        (right_max, right_max_start, right_max_end) = self.max_sa_recursive_helper(nums[len(nums)//2:])

        # can merge?
        if left_max_end == right_max_start:
            # see if merging makes sense
            if left_max > 0 and right_max > 0:
                return left_max + right_max

        return max(left_max, right_max)


s = Solution()
assert(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6) # looks good
#s.maxSubArray([2,1,-3,4,-1,2,1,-5,4])  # looks good
#s.maxSubArray([2,1,-4,2,-1,2,1,-4,4])  # looks good
assert(s.maxSubArray([-2,-1]) == -1)
