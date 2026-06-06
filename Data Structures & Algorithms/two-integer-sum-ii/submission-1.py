class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if target == numbers[i] + numbers[j]:
        #             return [i + 1, j + 1]

        # time: O(n^2)
        # space: O(1)

        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else: 
                return [i + 1, j + 1]

        # time: O(n)
        # space: O(1)
        