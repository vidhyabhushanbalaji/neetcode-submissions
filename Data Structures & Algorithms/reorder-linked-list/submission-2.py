# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next:
            if fast.next.next:
                fast = fast.next.next
            else:
                fast=fast.next
                break
            slow = slow.next
        
        prev = None
        temp = slow.next
        slow.next=None
        curr=temp
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
    
        curr = head
        while fast and curr:
            temp = curr.next
            nextFast = fast.next
            curr.next = fast
            curr.next.next = temp
            fast=nextFast
            curr = temp

        


