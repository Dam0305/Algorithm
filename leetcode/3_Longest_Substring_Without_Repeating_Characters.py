class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        tmp = []
        cnt = 0
        for i in range(len(s)):
            if s[i] in tmp:
                if cnt < len(tmp):
                    cnt = len(tmp)
                tmp = tmp[tmp.index(s[i])+1:]
                tmp.append(s[i])


            else:
                tmp.append(s[i])

        if cnt < len(tmp):
            cnt = len(tmp)

        return cnt






print(Solution().lengthOfLongestSubstring("abcabcbb"))