# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # optimized solution using divide and conquer
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists) , 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeLists(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

        # brute force
        # if not lists:
        #     return 

        # l = []
        # length = len(lists) 
        # for i in range(length):

        #     cur = lists[i]
        #     while cur:
        #         l.append(cur.val)
        #         cur = cur.next

        # l.sort()

        # head = ListNode(l[0])
        # curF = head

        # for i in range(1, len(l)):
        #     new_node = ListNode(l[i])
        #     curF.next = new_node
        #     curF = new_node

        # return head