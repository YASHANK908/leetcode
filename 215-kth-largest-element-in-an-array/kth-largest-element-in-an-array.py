class Solution(object):
    def findKthLargest(self, nums, k):
        def heapify_up(heap,index):
            parent=(index-1)//2
            while index>0 and heap[index]<heap[parent]:
                heap[index],heap[parent]=heap[parent],heap[index]
                index=parent
                parent=(index-1)//2
        def heapify_down(heap,index,n):
            
            while True:
                left= 2*index+1
                right=2*index+2
                smallest=index

                if left<n and heap[left]<heap[smallest]:
                    smallest=left
                if right<n and heap[right]<heap[smallest]:
                    smallest=right
                if smallest==index:
                    break
                heap[index],heap[smallest]=heap[smallest],heap[index]
                index=smallest

        def push(heap,val):
            heap.append(val)
            heapify_up(heap,len(heap)-1)
        def pop(heap):
            if len(heap)==1:
                return heap.pop()
            root=heap[0]
            heap[0]=heap.pop()
            heapify_down(heap,0,len(heap))
            return root
        heap=[]      
        for num in nums:
            push(heap,num)
            if len(heap)>k:
                pop(heap)
        return heap[0]        


        
        
        