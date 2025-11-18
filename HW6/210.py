from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        order = []

        while q:
            cur = q.popleft()
            order.append(cur)

            for nxt in adj[cur]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        if len(order) == numCourses:
            return order
        
        return []


Sol = Solution()

# Example 1
numCourses = 2
prerequisites = [[1,0]]
print(Sol.findOrder(numCourses, prerequisites)) # [0,1]

# Example 2
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Sol.findOrder(numCourses, prerequisites)) # [0,1,2,3] or [0,2,1,3]

# Example 3
numCourses = 1
prerequisites = []
print(Sol.findOrder(numCourses, prerequisites)) # [0]