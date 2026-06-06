class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow

        # time: O(n)
        # space: O(1)

        # visited = set()
        # for num in nums:
        #     if num in visited:
        #         return num
        #     visited.add(num)

        # time: O(n)
        # space: O(n)