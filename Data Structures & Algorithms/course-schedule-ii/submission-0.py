class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = defaultdict(set)
        visit = set()
        result = []
        for course, pre_course in prerequisites:
            course_map[course].add(pre_course)
        def dfs(course):
            if course in visit or course >= numCourses:
                return False
            if course_map[course] == ():
                return True
            
            visit.add(course)
            for preq in course_map[course]:
                if not dfs(preq):
                    return False
            visit.remove(course)
            course_map[course] = ()
            result.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return result