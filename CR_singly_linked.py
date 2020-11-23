# Competency Report
# Singly Linked List implementation


# class representing my node
class Node:
    
    data = None
    next_node = None #points to next node in the list

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return "<Node data: %s>" % self.data

class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
  
    # Adding new node with data at the head of the list
    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head # pointing new node to the head of the list
        self.head = new_node
    
    def search(self, key):
        # searching for node that matches the key
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


