from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # dic = {}
        #
        # for i in nums:
        #     dic[i] = dic[i] + 1 if i in dic else 1
        # sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        #
        # answer = []
        # for i in range(k):
        #     answer.append(sorted_dic[i][0])
        #
        # return answer

        return list(zip(*Counter(nums).most_common(k)))[0]


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
