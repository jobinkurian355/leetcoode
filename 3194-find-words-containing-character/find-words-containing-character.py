class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        l1 = []
        for i in range(len(words)):
            if x in words[i]:
                l1.append(i)
        return l1        
