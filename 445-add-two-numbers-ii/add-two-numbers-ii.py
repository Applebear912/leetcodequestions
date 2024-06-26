# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        cur = ListNode()
        result = cur
        dummy = None

        r_1 = None
        r_2 = None

        while l1:
            temp = l1
            l1 = l1.next
            temp.next = r_1
            r_1 = temp
        
        while l2:
            temp = l2
            l2 = l2.next
            temp.next= r_2
            r_2 = temp
        
        while r_1 or r_2 or carry:
            v1 = r_1.val if r_1 else 0
            v2 = r_2.val if r_2 else 0
            val = v1 + v2 + carry
            if val >= 10:
                val = val - 10
                carry = 1
            else:
                carry = 0
            cur.next = ListNode(val)
            r_1 = r_1.next if r_1 else None
            r_2 = r_2.next if r_2 else None
            cur = cur.next
        
        while result.next:
            temp = result.next
            result.next = result.next.next
            temp.next = dummy
            dummy = temp


        return dummy
        


            