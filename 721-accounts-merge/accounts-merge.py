from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent={}
        
        def find(x):
            if x not in parent:
                parent[x]=x
            if parent[x]!=x:
                parent[x]= find( parent[x])
            return parent[x]
        
        def union(x,y):
            px,py= find(x), find(y)

            if px!=py:
                 parent[py]=px
        
        email_to_name={}

        for account in accounts:
            name=account[0]
            first_email=account[1]

            for email in account[1:]:
                email_to_name[email]=name
                union(email,first_email)
        
        group=defaultdict(list)
        for email in email_to_name:
            root=find(email)
            group[root].append(email)


        res=[]
        for root,email in group.items():
            res.append([email_to_name[root]]+sorted(email))
        return res
        

        
        