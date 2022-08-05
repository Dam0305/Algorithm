class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        t = 1

        for i in range(len(nums)):
            result.append(t)
            t *= nums[i]

        t = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= t
            t *= nums[i]

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]
                                   ))
