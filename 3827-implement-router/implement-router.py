from collections import deque, defaultdict
import bisect

class Router(object):
    def __init__(self, memoryLimit):
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.unique = set()
        self.dest_timestamps = defaultdict(list)
        self.processed = defaultdict(int)

    def addPacket(self, source, destination, timestamp):
        pkt = (source, destination, timestamp)
        if pkt in self.unique:
            return False
        if len(self.queue) == self.memoryLimit:
            self.forwardPacket()
        self.queue.append(pkt)
        self.unique.add(pkt)
        self.dest_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self):
        if not self.queue:
            return []
        s, d, t = self.queue.popleft()
        self.unique.discard((s, d, t))
        self.processed[d] += 1
        return [s, d, t]

    def getCount(self, destination, startTime, endTime):
        if destination not in self.dest_timestamps:
            return 0
        timestamps = self.dest_timestamps[destination]
        start_idx = self.processed.get(destination, 0)
        l = bisect.bisect_left(timestamps, startTime, lo=start_idx)
        r = bisect.bisect_right(timestamps, endTime, lo=start_idx)
        return r - l
