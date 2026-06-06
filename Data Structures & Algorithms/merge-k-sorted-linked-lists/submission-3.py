# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # brute force
        if not lists:
            return 

        l = []
        length = len(lists) 
        for i in range(length):

            cur = lists[i]
            while cur:
                l.append(cur.val)
                cur = cur.next

        l.sort()

        head = ListNode(l[0])
        curF = head

        for i in range(1, len(l)):
            new_node = ListNode(l[i])
            curF.next = new_node
            curF = new_node

        return head
