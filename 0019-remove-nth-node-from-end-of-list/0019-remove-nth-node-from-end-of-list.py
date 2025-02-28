# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head

        listLen = 0

        while cur:

            cur = cur.next
            listLen += 1

        if listLen-n == 0:
            return head.next
        
        cur = head
        for i in range(listLen-1):
            if i+1 == listLen - n:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head


        