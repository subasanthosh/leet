# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        elif list2==None:
            return list1
        else:
            t = list1
            while t.next:
                t = t.next
            t.next = list2
            t = list1
            while t:
                t2 = t.next
                while t2:
                    if t.val>=t2.val:
                        temp = t.val
                        t.val = t2.val
                        t2.val = temp

                    t2 = t2.next
                t = t.next

            return list1


            