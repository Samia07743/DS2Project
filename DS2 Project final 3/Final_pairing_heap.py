class PairingHeapNode:
    def __init__(self, key, value):
        self.key = key          # the key of the node
        self.value = value      # the value associated with the key
        self.child = None       # the leftmost child of the node
        self.sibling = None     # the sibling of the node (the next node at the same level)

class PairingHeap:
    def __init__(self):
        self.root = None # the root node of the heap

    def is_empty(self): #This method checks if the pairing heap is empty
        return self.root is None #returns true if root node is none which indicates an empty pairing heap

    def merge(self, heap1, heap2): #this function merges two pairing heaps, heap1 and heap2 and returns the merged heap
        # Check if either heap is empty
        if heap1 is None:
            return heap2
        if heap2 is None:
            return heap1
        # If the root node of heap1 has a smaller key value than the root node of heap2
        if heap1.key < heap2.key:
            # Make the root of heap2 a child of root of heap1
            heap2.sibling = heap1.child #heap 2 ke sibling mei store heap 1s child
            # Make heap2 the new child of heap1
            heap1.child = heap2
            # Return the new heap1 with the merged heaps
            return heap1
        # If the root node of heap2 has a smaller key value than the root node of heap1
        else:
            # Make the root of heap1 a child of root of heap2
            heap1.sibling = heap2.child
            # Make heap1 the new child of heap2
            heap2.child = heap1
            # Return the new heap2 with the merged heaps
            return heap2

    def insert(self, key, value):
        # create a new PairingHeapNode with the given key and value
        new_node = PairingHeapNode(key, value)
        # merge the new node with the existing heap by setting the root to the result of the merge operation
        self.root = self.merge(self.root, new_node)

    def find_min(self):
        # if the heap is empty, return None
        if self.is_empty():
            return None
        # otherwise, return the key and value of the root node
        #print ("root",self.root.key)
        return self.root.value
        

    def delete_min(self):
        if self.is_empty(): # check if the heap is empty
            return None

        min_key = self.root.key  # store the minimum key
        min_value = self.root.value # store the corresponding value of minimum key

        if self.root.child is None: # if there are no children of the root
            self.root = None # set root to None
        else:
            children = [] # create an empty list to store children of the root
            current = self.root.child # start with the first child of the root
            while current is not None: # iterate over the children
                next_sibling = current.sibling # store the next sibling
                current.sibling = None # set the current sibling to None
                children.append(current) # append the current child to the list
                current = next_sibling # move to the next sibling

            self.root = None # set the root to None
            for child in children: # merge the children pairwise
                self.root = self.merge(self.root, child)
            print(self.display())

        return min_key,min_value # return the minimum key and corresponding value

    def display(self):
        
        def _display_helper(node): #Display the pairing heap in a list form using pre-order traversal
        
            if node is None:  #Recursive helper function for pre-order traversal
                return []
            result = [(node.key, node.value)]   # Add the value of the current node to the result list
            if node.child:
                result.extend(_display_helper(node.child))   #Recursively add values of child nodes
            if node.sibling:
                result.extend(_display_helper(node.sibling))   #Recursively add values of sibling nodes
            return result

        return _display_helper(self.root)


# heap=PairingHeap()
# heap.insert(1, 'zain')
# heap.insert(4, 'samia')
# heap.insert(5, 'dk')
# heap.insert(9, 'ayesha')
# heap.delete_min() 


    
 
    

 