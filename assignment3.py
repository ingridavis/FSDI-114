# 1. Implement a stack

# Create a class named "Stack" that allows you to:

# a. Check if it is empty

# b. Push a new item

# c. Pop an item

# d. Peek at the top item

# e. Return the size
class Queue2Stacks(object):

    def __init__(self):
        self.instack = []
        self.outstack = []
    
    def enqueue(self, element):

        self.instack.append(element)
    
    def dequeue(self):
        if not self.outstack:
            while self.instack:

                self.outstack.append(self.instack.pop())
            return self.outstack.pop()


# 2. Implement a queue

# Create a class named "Queue" that allows you to:

# a. Check if the queue is empty

# b. Enqueue

# c. Dequeue

# d. Return the size of the queue