from bisect import bisect_right

class Solution(object):
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1] * n
        full = {}
        dry_days = []

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
                ans[i] = 1
            else:
                if lake in full:
                    idx = bisect_right(dry_days, full[lake])
                    if idx == len(dry_days):
                        return []
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake
                    dry_days.pop(idx)
                full[lake] = i
        return ans
