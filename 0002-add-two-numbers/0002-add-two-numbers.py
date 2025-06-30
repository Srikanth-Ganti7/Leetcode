# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        n1 = 0
        firstSum = 0

        while temp1:
            unit = temp1.val
            firstSum = unit*(10**n1) + firstSum
            n1 += 1
            temp1 = temp1.next
        
        temp2 = l2
        n2 = 0
        secSum = 0

        while temp2:
            unit2 = temp2.val
            secSum = unit2*(10**n2) + secSum
            n2 += 1
            temp2 = temp2.next
        
        finalSum = firstSum + secSum

        if finalSum == 0:
            return ListNode(0)

        dummy = ListNode()
        cur = dummy

        while finalSum != 0:
            rem = finalSum % 10
            cur.next = ListNode(rem)
            cur = cur.next
            finalSum = finalSum // 10
        
        return dummy.next

        