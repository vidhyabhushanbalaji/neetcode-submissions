# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = ListNode(-1)
        start.next=head
        left = start
        right = start.next

        while right:
            count = 0
            while count!=k-1 and right:
                count+=1
                right =right.next
            
            if count!=k-1 or not right:
                return start.next

            temp = left.next
            left.next = right
            left = temp
            firstleft = temp

            prev = right.next

            while left!=right:
                temp = left.next
                left.next=prev
                prev = left
                left = temp
            nextRight = right.next
            left.next = prev
            right = nextRight
            left = firstleft
            #for i in range(k-1):
            #    left = left.next
            
        return start.next
        