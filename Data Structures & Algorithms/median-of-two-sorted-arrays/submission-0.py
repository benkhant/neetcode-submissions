class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []

        p1, p2 = 0, 0

        while p1 <= len(nums1) - 1 and p2 <= len(nums2) - 1:
            if nums1[p1] <= nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1

        while p1 < len(nums1):
            res.append(nums1[p1])
            p1 += 1
        while p2 < len(nums2):
            res.append(nums2[p2])
            p2 += 1

        if len(res) % 2 == 0:
            f = res[(len(res) - 1) // 2]
            s = res[(len(res)) // 2]
            return (f + s) / 2
        else:
            return res[(len(res) - 1) // 2]