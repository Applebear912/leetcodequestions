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
        head = ListNode()
        current = head
        # initiate empty head to start

        while list1 and list2:
            # when one list reach to the end there is no need to continue the loop
            if list1.val < list2.val:
                # small one goes into the new list, having current head pointing to it
                current.next = list1
                # 
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 or list2
        return head.next

                
                               
        