from itertools import permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answer = []
        for i in permutations(nums):
            answer.append(list(i))


        return answer



print(Solution().permute([1,2,3]))