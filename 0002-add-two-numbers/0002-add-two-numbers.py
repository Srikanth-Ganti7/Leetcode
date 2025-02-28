# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode
        
        temp1 = l1
        num1 = 0
        count = 0
        while temp1:
            num1 = (num1) + (temp1.val*(10**count))
            temp1 = temp1.next
            count += 1
        print(num1)

        temp2 = l2
        num2 = 0
        count2 = 0
        while temp2:
            num2 = (num2) + (temp2.val*(10**count2))
            temp2 = temp2.next
            count2+=1
        
        print(num2)

        final_num = num1+num2
        print(final_num)

        if final_num == 0:
            return ListNode(0)

        tail = dummy
        while final_num:
            n = final_num % 10
            final_num = final_num // 10
            tail.next = ListNode(n)
            tail = tail.next
        
        return dummy.next










         

        