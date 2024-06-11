# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # find mid node, slow pointer
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
    
        # reverse the 2nd half linked list
        new_head_2nd_half = None
        while slow:
            temp = slow
            slow = slow.next
            temp.next = new_head_2nd_half
            new_head_2nd_half = temp
        
        # check if it is palidrome
        left, right = head, new_head_2nd_half
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True