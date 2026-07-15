class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashMap:
            self.hashMap[key] = []
        self.hashMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.hashMap:
            return res
        l, r = 0, len(self.hashMap[key]) - 1
        while l <= r:
            mid = (l + r) // 2
            if timestamp < self.hashMap[key][mid][1]:
                r = mid - 1
            elif timestamp > self.hashMap[key][mid][1]:
                l = mid + 1
            else:
                return self.hashMap[key][mid][0]
        return self.hashMap[key][r][0] if r >= 0 else ""

        # Time: O(logn)
        # Space: O(n)

        # res = ""
        # if key not in self.hashMap:
        #     return res
        # for val, ts in self.hashMap[key]:
        #     if ts <= timestamp:
        #         res = val             
        # return res

        # Time: O(n) for get
        # Space: O(n)