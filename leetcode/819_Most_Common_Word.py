class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        stopwords = '~`!@#$%^&*()-_=+\[\]\{\},./<>?;\':\"'
        paragraph = paragraph.lower()

        for stopword in stopwords:
            if stopword in paragraph:
                paragraph = paragraph.replace(stopword, " ")
        for ban in banned:
            if ban in paragraph:
                paragraph = paragraph.replace(ban, "")

        paragraph = paragraph.split()

        return Counter(paragraph).most_common(1)[0][0]
