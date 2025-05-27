
#define MAX 50000

typedef struct {
    int left[MAX];
    int right[MAX];
    int sizeleft;
    int sizeright;
} MedianFinder;


MedianFinder* medianFinderCreate() {
    MedianFinder* obj= (MedianFinder*) malloc(sizeof(MedianFinder));
    obj->sizeleft=0;
    obj->sizeright=0;
    return obj; 
}

void maxHeapifyUp(int* heap, int index) {
    while (index > 0 && heap[index] > heap[(index - 1) / 2]) {
        int temp = heap[index];
        heap[index] = heap[(index - 1) / 2];
        heap[(index - 1) / 2] = temp;
        index = (index - 1) / 2;
    }
}

 
void minHeapifyUp(int* heap, int index) {
    while (index > 0 && heap[index] < heap[(index - 1) / 2]) {
        int temp = heap[index];
        heap[index] = heap[(index - 1) / 2];
        heap[(index - 1) / 2] = temp;
        index = (index - 1) / 2;
    }
}

void maxHeapifyDown(int* heap, int size, int index) {
    while (2 * index + 1 < size) {
        int largest = index, left = 2 * index + 1, right = 2 * index + 2;
        if (heap[left] > heap[largest]) largest = left;
        if (right < size && heap[right] > heap[largest]) largest = right;
        if (largest == index) break;
        int temp = heap[index];
        heap[index] = heap[largest];
        heap[largest] = temp;
        index = largest;
    }
}

void minHeapifyDown(int* heap, int size, int index) {
    while (2 * index + 1 < size) {
        int smallest = index, left = 2 * index + 1, right = 2 * index + 2;
        if (heap[left] < heap[smallest]) smallest = left;
        if (right < size && heap[right] < heap[smallest]) smallest = right;
        if (smallest == index) break;
        int temp = heap[index];
        heap[index] = heap[smallest];
        heap[smallest] = temp;
        index = smallest;
    }
}


void medianFinderAddNum(MedianFinder* obj, int num) {
  if(obj->sizeleft==0 || num<=obj->left[0]){
    obj->left[obj->sizeleft++]=num;
     maxHeapifyUp(obj->left,obj->sizeleft-1);
      
  }  
  else{
    obj->right[obj->sizeright++]=num;
     minHeapifyUp(obj->right,obj->sizeright-1);
  }

  if (obj->sizeleft > obj->sizeright + 1) {
    obj->right[obj->sizeright++] = obj->left[0];
    minHeapifyUp(obj->right, obj->sizeright - 1);
    obj->left[0] = obj->left[--obj->sizeleft];
    maxHeapifyDown(obj->left, obj->sizeleft, 0);
} else if (obj->sizeright > obj->sizeleft) {
    obj->left[obj->sizeleft++] = obj->right[0];
    maxHeapifyUp(obj->left, obj->sizeleft - 1);
    obj->right[0] = obj->right[--obj->sizeright];
    minHeapifyDown(obj->right, obj->sizeright, 0);
}
}

double medianFinderFindMedian(MedianFinder* obj) {
   if(obj->sizeleft==obj->sizeright){
    return (obj->left[0]+obj->right[0])/2.0;
   } 
   else{
    return obj->left[0];
   }
}

void medianFinderFree(MedianFinder* obj) {
    free(obj);
}

// /**
//  * Your MedianFinder struct will be instantiated and called as such:
//  * MedianFinder* obj = medianFinderCreate();
//  * medianFinderAddNum(obj, num);
 
//  * double param_2 = medianFinderFindMedian(obj);
 
//  * medianFinderFree(obj);
// */
 