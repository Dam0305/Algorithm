class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        num = []
        str = []
        for i in logs:
            if i.split()[1].isdigit():
                num.append(i)
            else:
                str.append(i)

        str.sort(key=lambda x:(x.split()[1:], x.split()[0]))
        return str + num
