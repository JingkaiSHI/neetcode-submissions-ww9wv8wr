# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # at this point, slow is the head of the linked list we want to reverse
        # reverse the linkedlist that starts at slow
        # prev will be the actual head of second list to join
        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        # head is l1, prev is l2, join head first
        while prev.next:
            tmp1, tmp2 = head.next, prev.next
            head.next = prev
            prev.next = tmp1
            head, prev = tmp1, tmp2



        