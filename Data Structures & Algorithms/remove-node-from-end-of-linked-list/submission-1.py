# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # brute force
        # if not head: 
        #     return

        # length = 0
        # cur = head
        # while cur:
        #     length += 1
        #     cur = cur.next

        # removeIndex = length - n
        # if removeIndex == 0:
        #     return head.next
            
        # cur = head
        # for i in range(length - 1):
        #     if (i + 1) == removeIndex:
        #         cur.next = cur.next.next
        #         break
        #     cur = cur.next

        # return head

        # optimized using two pointers
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
    