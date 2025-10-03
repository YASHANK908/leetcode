class KthLargest(object):

    def __init__(self, k, nums):
        self.k=k
        self.heap=[]
        for num in nums:
            self.push(num)
            if len(self.heap)>k:
                self.pop()


    def push(self,val):
        self.heap.append(val)
        self.heapify_up(len(self.heap)-1)

    def pop(self):
        if len(self.heap)==1:
            self.heap.pop()
        root=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapify_down(0)
        return root    

    def heapify_up(self,index):
        parent=(index-1)//2
        while index>0 and self.heap[index]<self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]   
            index=parent
            parent=(index-1)//2
    def heapify_down(self,index):
        n=len(self.heap)
        while True:
            left=2*index+1
            right=2*index+2
            smallest=index 
            if left<n and self.heap[left]<self.heap[smallest]:
                smallest=left
            if right<n and self.heap[right]<self.heap[smallest]:
                smallest=right
            if smallest==index:
                break
            self.heap[index],self.heap[smallest]=self.heap[smallest],self.heap[index]
            index=smallest

                     

       
        

    def add(self, val):
        self.push(val)
        if len(self.heap)>self.k:
            self.pop()
        return self.heap[0]    
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)