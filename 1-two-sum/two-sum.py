class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i,j in enumerate(nums):
            difference = target- j
            if difference in hash_map:
                return [hash_map[difference],i]
            hash_map[j] = i    

