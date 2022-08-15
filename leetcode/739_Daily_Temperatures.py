class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []
        answer = [0 for _ in range(len(temperatures))]

        for i , tem in enumerate(temperatures):
            while stack and tem > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)


        return answer





print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
