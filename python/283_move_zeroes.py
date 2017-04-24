class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            raise Exception("Invalid input")
        leftMostZeroPos = 0
        runner = 0
        while runner < len(nums):
            if nums[runner] != 0:
                tmp = nums[runner]
                nums[runner] = nums[leftMostZeroPos]
                nums[leftMostZeroPos] = tmp
                leftMostZeroPos += 1
            runner += 1
