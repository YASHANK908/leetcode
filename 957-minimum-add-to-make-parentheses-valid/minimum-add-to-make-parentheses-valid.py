class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count_open=0
        add_req=0

        for ch in s:
            if ch=='(':
                count_open+=1
            else:
                if count_open==0:
                    add_req+=1
                else:
                    count_open-=1
        return count_open+add_req

        