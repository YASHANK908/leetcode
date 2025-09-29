class Solution(object):
    def minRemoveToMakeValid(self, s):
        res=[]
        balance=0

        for ch in s:
            if ch=='(':
                balance+=1
                res.append(ch)
            elif ch==')':
                if balance==0:
                    continue
                balance-=1
                res.append(ch)
            else:
                res.append(ch)

        final=[]
        open_to_remove=balance
        for ch in reversed(res):
            if ch=='(' and open_to_remove>0:
                open_to_remove-=1
            else:
                final.append(ch)
        return "".join(reversed(final))            