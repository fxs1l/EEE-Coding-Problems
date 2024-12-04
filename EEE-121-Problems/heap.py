class MinHeap:
    def __init__(self):
          #Filler for zeroth element to have the actual start of indexing to our min heap at arr[1]
        self.arr = [None] 
        self.size = 0

    # Part A.
    # Fill in the ff. functions such that, given an array implementation arr
    # of a complete tree and a node at arr[idx], the following functions
    # correctly return the indices of the left child, right child, and parent
    # of the given node. Assume that the root node is at arr[1] (NOT arr[0]).

    def _left_child(self, idx):
        return int(2 * (idx) ) 
    def _right_child(self, idx):
        return int(2 * (idx) + 1)
    def _parent(self, idx):
        return int(idx/2) 

    def _swap_nodes(self, i, j):
        '''Helper function for swapping two nodes at indices i and j.'''
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def _bubble_down(self, idx):
        '''
        Bubbles down a node at arr[idx] to preserve min-heap properties.

        Specifically, a node needs to be moved down the heap if its value is
        greater than either of its children's values. To ensure that the
        least node is at the top of the heap, the current node is swapped
        with the lesser of its two children.
        '''
        
        # Part B.
        # This is a standard implementation of a bubble down algorithm for min heap. 
        # Modify this accordingly to accomodate Constraint #3 which indicates
        # that you need to order alphabetically regardless of character case.
        
        left_idx = self._left_child(idx)
        right_idx = self._right_child(idx)

        if (left_idx > self.size):
            return

        elif (right_idx > self.size):
            left_val = self.arr[left_idx].capitalize()

            if (left_val < self.arr[idx].capitalize()):
                self._swap_nodes(left_idx, idx)

        else:
            left_val = self.arr[left_idx].capitalize()
            right_val = self.arr[right_idx].capitalize()

            if (left_val < self.arr[idx].capitalize() and left_val < right_val):
                self._swap_nodes(left_idx, idx)
                self._bubble_down(left_idx)
            elif (right_val < self.arr[idx].capitalize() and right_val < left_val):
                self._swap_nodes(right_idx, idx)
                self._bubble_down(right_idx)

    def _bubble_up(self, idx):
        '''
        Bubbles up a node at arr[idx] to preserve min-heap properties.

        Specifically, a node needs to be moved up the heap if its value is
        less than its parent's.
        '''
        
        # Part C.
        # This is a standard implementation of a bubble up algorithm for min heap. 
        # Modify this accordingly to accomodate Constraint #3 which indicates
        # that you need to order alphabetically regardless of character case.
        parent_idx = self._parent(idx)
        parent_val = self.arr[parent_idx].capitalize()

        if (idx == 1):
            return

        if (self.arr[idx].capitalize() < parent_val):
            self._swap_nodes(parent_idx, idx)

            if (parent_idx > 1):
                self._bubble_up(parent_idx)

    # Part C.
    # Complete the following function to perform the following operations:
    # - pop the top node from the min-heap
    #   (i.e. remove the node and return its value)
    # - swap nodes in the heap to preserve the heap's order and shape
    # - adjust the count for the number of nodes in the heap

    def extract(self):
        '''Removes the minimum element from the heap and returns its value.'''
        # Extract the results by doing something here. Hint: swap nodes and pop the array
        result = self.arr[1]
        self._swap_nodes(1, self.size)
        self.arr.pop(self.size)

        self.size = len(self.arr)-1 # No. of nodes after the top node is popped

        if self.size > 1: # If the heap still contains nodes...
            self._bubble_down(1)
        return result

    # Part D.
    # Complete the following function to perform the following operations:
    # - insert a new node (with value val) into the heap
    # - swap nodes in the heap to preserve the heap's order and shape
    # - adjust the count for the number of nodes in the heap

    def insert(self, val):
        '''Inserts a new value into the heap.'''
        idx = self.size+1 # Index where the new value should be placed
        self.arr.insert(idx, val)
        self.size = len(self.arr)-1 # No. of nodes after insertion

        if self.size > 1: # If the new node is not the root...
            self._bubble_up(self.size)


# NOTE: The following statements in main check for the correctness of
#       your implementation. Do not modify anything beyond this point!
if __name__ == '__main__':
    n = int(input())
    ls = list()

    for i in range(n):
        ls.append(input().rstrip())

    myHeap = MinHeap()

    for x in ls:
        myHeap.insert(x)

    while(myHeap.size != 0):
        print(myHeap.extract())
