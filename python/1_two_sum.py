class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            raise Exception("Empty list")
        visited = {}
        for i in xrange(len(nums)):
            if target-nums[i] in visited:
                return [visited[target-nums[i]], i]
            else:
                visited[nums[i]] = i
        raise Exception("Not found")
                