# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        current = dummy

        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            res = val1 + val2 + carry
            carry = res//10
            res = res%10

            resNode = ListNode(res)
            current.next = resNode
            current = resNode

            if l1 and l2:
                l1 = l1.next
                l2 = l2.next
            
            elif l1:
                l1 = l1.next
            
            elif l2:
                l2 = l2.next
        return dummy.next