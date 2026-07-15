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
        for val, ts in self.hashMap[key]:
            if ts <= timestamp:
                res = val             
        return res

        # Time: O(n) for get
        # Space: O(n)