# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 == None) and (list2 == None):
            return list1

        if (list1 == None):
            return list2
        
        if (list2 == None):
            return list1

        dummy = ListNode()
        tail = dummy

        cur1 = list1
        cur2 = list2

        while (cur1 != None) and (cur2 != None):
            if cur1.val >= cur2.val:
                tail.next = cur2
                tail = tail.next
                cur2 = cur2.next
                
            else:
                tail.next = cur1
                tail = tail.next
                cur1 = cur1.next

        tail.next = cur1 or cur2

        return dummy.next

