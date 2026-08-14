class Twitter:

    def __init__(self):
        self.tweet = defaultdict(list)
        self.followMap = defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweet[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweet:
                idx = len(self.tweet[followeeId]) - 1
                count, tweetId = self.tweet[followeeId][idx]
                heapq.heappush(heap, (count, tweetId, followeeId, idx - 1))

        res = []
        while heap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweet[followeeId][idx]
                heapq.heappush(heap, (count, tweetId, followeeId, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

    # Time: O(klogk)
    # Space: O(k)
