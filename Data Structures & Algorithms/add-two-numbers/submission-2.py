# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        currLeft = l1
        currRight = l2
        
        while currLeft or currRight or carry>0:
            left = 0
            if currLeft:
                left = currLeft.val

            right = 0
            if currRight:
                right = currRight.val

            add= carry+ left + right
            carry = add//10
            val = add%10

            currLeft.val = val

            if not currLeft.next and ((currRight and currRight.next) or carry>0):
                currLeft.next = ListNode(0)
                currLeft = currLeft.next
            elif currLeft:
                currLeft = currLeft.next
            if currRight:
                currRight = currRight.next
            
        return l1
                              