# Competency Report
# Doubly Linked List implementation


# class representing my node
class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node
        

    def __repr__(self):
        return "<Node data: %s>" % self.data

# class representing my Double Linked List
class LinkedList:

    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

     # adding new nodes to the head   
    def push(self, data):
        # Making the new node the head, and anything previous as none
        new_head = Node(data, prev_node=None, next_node=self.head) 
        
        if not self.is_empty():
            self.head.prev_node = new_head #making prev of head node the new head node
        self.head= new_head

    def search(self, key):
        current = self.head # points to the head of list
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def __repr__(self):
        # string representation of the list.
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node

        return '-> '.join(nodes)


