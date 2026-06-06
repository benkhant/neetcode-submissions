class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

        # Time: O(n)
        # Space: O(1)

        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1

        # maj = float('-inf')

        # for count in freq:
        #     if freq[count] > maj:
        #         maj = freq[count]
        #         maj_element = count

        # return maj_element

        # Time: O(n)
        # Space: O(n)