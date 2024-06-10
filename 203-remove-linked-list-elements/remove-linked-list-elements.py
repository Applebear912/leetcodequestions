# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev, curr = None, head
        while curr:
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
        # dummy = ListNode(0)
        # dummy.next = head
        
        # prev, cur = dummy, head
        # while cur:
        #     if cur.val == val:
        #         prev.next = cur.next 
        #     else:
        #         prev = cur
        #     cur = cur.next
        # return dummy.next