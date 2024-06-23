# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        p1 = list1
        p2 = list2

        new_ll_head = None
        tail = None
        while p1 and p2:
            if p1.val < p2.val:
                if not new_ll_head:
                    new_ll_head = p1
                    tail = p1
                else:
                    tail.next = p1
                    tail = tail.next
                p1 = p1.next
            else:
                if not new_ll_head:
                    new_ll_head = p2
                    tail = p2
                else:
                    tail.next = p2
                    tail = tail.next
                p2 = p2.next
        if p1:
            if not new_ll_head:
                new_ll_head = p1
                tail = p1
            else:
                tail.next = p1
        if p2:
            if not new_ll_head:
                new_ll_head = p2
                tail = p2
            else:
                tail.next = p2
        return new_ll_head