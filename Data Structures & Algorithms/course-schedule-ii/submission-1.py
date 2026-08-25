class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for course, pre in prerequisites:
            prereq[course].append(pre)

        visiting = set()
        visited = set()
        res = []

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            visited.add(course)
            res.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return res

    # Time: O(V+E)
    # Space: O(V+E)