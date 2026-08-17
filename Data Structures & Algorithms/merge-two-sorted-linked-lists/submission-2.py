# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if (list1.val<list2.val):
            head = list1
            nextL1 = list1.next
            nextL2 = list2
        else:
            head = list2
            nextL1 = list1
            nextL2 = list2.next
        
        curr = head

        while curr:
            if not nextL1:
                curr.next= nextL2
                break
            if not nextL2:
                curr.next= nextL1
                break
            if (nextL1.val)<(nextL2.val):
                curr.next = nextL1
                curr = nextL1
                nextL1 = nextL1.next
            else:
                curr.next = nextL2
                curr = nextL2
                nextL2 = nextL2.next
        
        return head
            