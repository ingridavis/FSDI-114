class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_len(head):
        node= head
        size = 0
        while True:
            if node:
                size += 
                node = node.next
            else:
                break

    if __name__ == "__main__":
        head = Node(1)
        node = head

        for index in range(1,10):
            node.next= Node(index)
            node = node.next
        
        print("The size of my list is : %s" % get_len(head))

        node = head
        next_node = head.next
        new_node = Node(10)
        node.next = new_node
        node.next.next = next.node

        print("The size of my list is : %s" % get_len(head))
        print_list(head)