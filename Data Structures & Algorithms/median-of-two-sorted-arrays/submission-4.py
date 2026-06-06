class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a

        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            Aleft = a[i] if i >= 0 else float('-infinity')
            Aright = a[i + 1] if (i + 1) < len(a) else float('infinity')
            Bleft = b[j] if j >= 0 else float('-infinity')
            Bright = b[j + 1] if (j + 1) < len(b) else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1

        # time: O(log(min(a, b)))
        # space: O(1)             

        # res = []

        # p1, p2 = 0, 0

        # while p1 <= len(nums1) - 1 and p2 <= len(nums2) - 1:
        #     if nums1[p1] <= nums2[p2]:
        #         res.append(nums1[p1])
        #         p1 += 1
        #     else:
        #         res.append(nums2[p2])
        #         p2 += 1

        # while p1 < len(nums1):
        #     res.append(nums1[p1])
        #     p1 += 1
        # while p2 < len(nums2):
        #     res.append(nums2[p2])
        #     p2 += 1

        # if len(res) % 2 == 0:
        #     f = res[(len(res) - 1) // 2]
        #     s = res[(len(res)) // 2]
        #     return (f + s) / 2
        # else:
        #     return res[(len(res) - 1) // 2]

        # time: O(m + n)
        # space: O(m + n)