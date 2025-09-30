class Solution(object):
    def calPoints(self, operations):
        stack=[]
        total=0
        for op in operations:
            if op=='+':
                score=stack[-1]+stack[-2]
                stack.append(score)
                total+=score
            elif op=='D':
                score=2*stack[-1]
                stack.append(score)
                total+=score
            elif op=='C':
                total-=stack.pop()
            else:
                score=int(op)
                stack.append(score)
                total+=score
        return total                    
        