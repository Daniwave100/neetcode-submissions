# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return head

        cur = head.next # [1, 2, 3]
        head.next = None # [0]

        while cur:
            reference = cur.next # [2, 3]
            cur.next = head
            head = cur
            cur = reference

        return head