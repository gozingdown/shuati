class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            raise Exception('invalid input')
        vote = 0
        candidate = None
        for x in nums:
            if x == candidate:
                vote += 1
            else:
                vote -= 1
                if vote <= 0:#<= because the first value is always different than None
                    candidate = x
                    vote = 1
        return candidate
