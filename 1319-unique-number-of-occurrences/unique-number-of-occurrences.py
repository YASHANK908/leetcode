class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count=Counter(arr)
        freq=list(count.values())
        new_set=set(count.values())
        if len(freq)!=len(new_set):
            return False
        else:
            return True
        