from itertools import combinations


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        arr = [i for i in range(1, n + 1)]
        answer = []
        for i in combinations(arr, k):
            answer.append(list(i))

        return answer


print(Solution().combine(4, 2))
