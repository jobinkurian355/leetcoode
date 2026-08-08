class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        l1 = []
        n = len(words)
        for i,k in enumerate(words):
            for j in k:
                if j == x:
                    l1.append(i)
                    break     
        return l1        
