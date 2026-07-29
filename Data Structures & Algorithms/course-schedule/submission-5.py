class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(set)
        for course, preq in prerequisites:
            course_map[course].add(preq)
        visit = set()

        def dfs(course):
            if course >= numCourses or course in visit:
                return False
            if course_map[course] == ():
                return True
            
            visit.add(course)
            for preq in course_map[course]:
                if not dfs(preq):
                    return False
            visit.remove(course)
            course_map[course] = ()
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True