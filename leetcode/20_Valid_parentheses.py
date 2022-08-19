class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 1:
            return False
        stack = []

        for i in s:
            if i == '(':
                stack.append(i)
            elif i == '{':
                stack.append(i)
            elif i == '[':
                stack.append(i)
            elif i == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif i == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif i == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()

        return True if len(stack) == 0 else False


print(Solution().isValid("(]"))