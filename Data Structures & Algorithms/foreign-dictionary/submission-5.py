class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {}

        for word in words:
            for ch in word:
                if ch not in indegree:
                    indegree[ch] = 0

        n = len(words)
        for i in range(n - 1):
            w1 = words[i]
            w2 = words[i + 1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break

        q = deque([ch for ch in indegree if indegree[ch] == 0])
        order = []

        while q:
            ch = q.popleft()
            order.append(ch)
            for nei in adj[ch]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(order) == len(indegree):
            return "".join(order)
        else:
            return ""

        # time: O(w * c), w = number of words, c = numbers of char
        # space: O(w * c), w = number of words, c = numbers of char
