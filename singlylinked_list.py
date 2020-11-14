# simple python program to intro a linked list
class Node:
# function to initialize the node object
    def __init__(self, data):
        self.data = data # assign data
        self.next = None #initilize next as null
# linked List class contains a node object
class LinkedList:
    #Function to initialize head
    def __init__(self):
        self.head = None

    def remove(head, key):
        node = head
        while True:
            if node:                    #node 1
                node = node.next        #node 2
            else:
                break
                
            if node.next.data == key:   # if (2).next.data == 3
                temp = node             # temp = 2
                node = node.next.next   # node = (2).(3).(4)
                temp.next  = node       # (2).next = 4
                return head

        return node
            

        
#Code execution starts here
# Session3 challenge: make a for loop that prints 123
if __name__ == 'main':
    
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

# link first node with second and so on.
llist.head.next = second

second.next = third

my_node = llist.head
while True:
    if my_node:
        print(my_node.data)
        my_node = my_node.next
    else:
        break
    