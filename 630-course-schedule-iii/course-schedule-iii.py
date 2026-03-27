import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x:x[1])
        maxheap=[]
        currenttime=0

        for duration,lastday in courses:
            currenttime+=duration
            heapq.heappush(maxheap,-duration)

            if currenttime>lastday:
                longest=-heapq.heappop(maxheap)
                currenttime-=longest
        return len(maxheap)
        