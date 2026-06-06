# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: 
            return

        # length = 0
        # current = head
        # while current:
        #     current = current.next
        #     length += 1

        # nthNode = length - n # 2
        # count = 0

        # cur = head
        # while cur:
        #     cur = cur.next
        #     count += 1
        #     if count == nthNode - 1:
        #         cur = cur.next.next
        # return head
        
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        removeIndex = length - n
        if removeIndex == 0:
            return head.next
            
        cur = head
        for i in range(length - 1):
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next

        return head