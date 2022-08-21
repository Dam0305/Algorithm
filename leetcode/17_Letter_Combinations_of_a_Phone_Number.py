from itertools import combinations

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(index, path):
            if len(path) == len(digits):
                arr.append(path)
                return


            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)


        if len(digits) == 0:
            return []

        dic = {"2":'abc', "3":'def',"4":'ghi',"5":'jkl',"6":'mno',"7":'pqrs',"8":'tuv',"9":'wxyz'}

        arr = []
        dfs(0, "")
        return arr




print(Solution().letterCombinations('23'))