class Solution(object):
    def parseBoolExpr(self, expression):
        stack=[]
        for ch in expression:
            if ch==",":
                continue
            elif ch!=')':
                stack.append(ch)
            else:
                vals=[]
                while stack[-1]!='(':
                    vals.append(stack.pop())
                stack.pop()
                op=stack.pop()
                if op=='!':
                    res='t' if vals[0]=='f' else 'f'
                elif op=='&':
                    res='t' if all(v=='t' for v in vals) else 'f'
                elif op=='|':
                    res='t' if any(v=='t' for v in vals) else 'f' 
                stack.append(res)
        return stack[-1]=='t'           

        