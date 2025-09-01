import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        # ensure floating point division
        def delta(p, t):
            return float(t - p) / (t * (t + 1))

        heap = [(-delta(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            neg_d, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            heapq.heappush(heap, (-delta(p, t), p, t))

        total = 0.0
        for _, p, t in heap:
            total += float(p) / t

        return total / len(classes)