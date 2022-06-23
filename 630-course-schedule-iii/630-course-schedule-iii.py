class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        courses.sort(key = lambda x: x[1])
        q = []
        time = 0
        ans = 0
        
        for duration, endTime in courses:
            if time + duration <= endTime:
                heappush(q,-duration)
                time += duration
            else:
                if q and duration < -q[0]:
                    saveTime = time + q[0]
                    if saveTime + duration <= endTime:
                        heappushpop(q,-duration)
                        time = saveTime + duration
            ans = max(ans, len(q))

        return ans
                        
                        