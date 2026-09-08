# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(-1, head)

        slow=head
        fast = head

        while fast.next:
            if fast.next.next:
                fast=fast.next.next
            else:
                fast=fast.next
            
            slow=slow.next

        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        slow=dummy.next

        while slow.next and fast.next:
            nextSlow = slow.next
            nextFast = fast.next

            slow.next = fast
            slow.next.next = nextSlow

            slow = nextSlow
            fast = nextFast

