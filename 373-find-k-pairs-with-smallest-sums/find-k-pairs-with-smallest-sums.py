class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        def heapify_up(heap,index):
            parent=(index-1)//2
            while index>0 and heap[index][0]<heap[parent][0]:
                heap[index],heap[parent]=heap[parent],heap[index]
                index=parent
                parent=(index-1)//2
        def heapify_down(heap,index):
            n=len(heap)
            while True:
                left=2*index+1
                right=2*index+2
                smallest=index
                if left<n and heap[left][0]<heap[smallest][0]:
                    smallest=left
                if right<n and heap[right][0]<heap[smallest][0]:
                    smallest=right
                if smallest==index:
                    break
                heap[index],heap[smallest]=heap[smallest],heap[index]
                index=smallest

        def heappush(heap,val):
            heap.append(val)
            heapify_up(heap,len(heap)-1)
        def heappop(heap):
            if len(heap)==1:
                return heap.pop()
            root=heap[0]
            heap[0]=heap.pop()
            heapify_down(heap,0)
            return root
        if not nums1 or not nums2:
            return []
        heap=[]
        res=[]
        for i in range(min(len(nums1),k)):
            heappush(heap,(nums1[i]+nums2[0],i,0))  
        while heap and len(res)<k:
            s,i,j=heappop(heap)
            res.append((nums1[i],nums2[j]))

            if j+1 <len(nums2):
                heappush(heap,(nums1[i]+nums2[j+1],i,j+1)) 
        return res                                                     

         