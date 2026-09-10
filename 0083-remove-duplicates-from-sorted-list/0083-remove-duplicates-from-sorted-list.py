# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t = head
        if not t:
            return head
        while t.next:
            if t.val == t.next.val:
                temp = t.next
                while temp and temp.val==t.val:
                    temp = temp.next
                if temp:
                    t.next = temp
                else:
                    t.next = None
            if not t.next:
                break
            t = t.next

        return head