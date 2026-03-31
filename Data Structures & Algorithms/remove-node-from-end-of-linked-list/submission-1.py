# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # I think 2-pass is just the method we can apply
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        actual_n = length - n
        if actual_n == 0:
            return head.next
        curr = head
        for i in range(length - 1):
            if (i + 1) == actual_n:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
        