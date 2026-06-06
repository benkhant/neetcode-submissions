# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # # brute force
        # if not head: 
        #     return 
        # # collect node references
        # cur = head
        # nodes = []
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next

        # # rewire with two pointers
        # l, r = 0, len(nodes) - 1
        # while l < r:
        #     nodes[l].next = nodes[r]
        #     l += 1
        #     if l == r: 
        #         break
        #     nodes[r].next = nodes[l]
        #     r -= 1

        # # terminate the list
        # nodes[l].next = None       

        # optimized solution
        # find the middle of the list using slow/fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # at the end, slow is pointing to the middle of the node

        # reverse the second half of the list
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next # store the next node
            second.next = prev # reverse current node's pointer
            prev = second # move prev forward
            second = tmp # move to the next node
        # after this loop, prev points to the head of the reversed second half

        # merge the two halves

        first, second = head, prev #  first = first half, second = reversed half
        while second: 
            # save the next pointers so we don't lose the rest of the list
            tmp1, tmp2 = first.next, second.next

            # rewire links to interleave nodes from first and second halves
            first.next = second
            second.next = tmp1

            # move both pointers forward
            first, second = tmp1, tmp2        