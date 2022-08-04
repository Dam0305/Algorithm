from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dic = defaultdict(list)

        for i in range(len(strs)):
            word = ''.join(sorted(strs[i]))
            dic[word].append(strs[i])


        answer = []
        for i in dic:
            answer.append(dic[i])

        return answer


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
