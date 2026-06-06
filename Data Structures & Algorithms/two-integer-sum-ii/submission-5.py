class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1]
                
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        
        # time: O(n^2)
        # space: O(1)