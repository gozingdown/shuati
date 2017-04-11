# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            raise Exception("invalid input")
        left_runner = l1
        right_runner = l2
        result = ListNode(-1)
        result_runner = result
        carry_over = 0
        while left_runner or right_runner:
            left = left_runner.val if left_runner else 0
            right = right_runner.val if right_runner else 0
            sum = left + right + carry_over
            carry_over = sum / 10
            result_runner.next = ListNode(sum % 10)
            result_runner = result_runner.next
            left_runner = left_runner.next if left_runner else None
            right_runner = right_runner.next if right_runner else None
        if carry_over > 0:
            result_runner.next = ListNode(carry_over)
        return result.next