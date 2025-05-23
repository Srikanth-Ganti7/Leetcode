# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            cur = groupPrev.next

            prev = kth.next

            while cur != groupNext:
                temp = cur.next
                cur.next = prev

                prev = cur
                cur = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return dummy.next
        

    def getKth(self,curr,k):
        while curr and k>0:
            curr = curr.next
            k -= 1
        return curr
        