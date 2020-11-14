# HW challenge 

class Queue2Stacks:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self, element):
        pass

    def dequeue(self):
        pass

def test():
# Note: should print vertically
    q = Queue2Stacks()
    for i in range(5):
        q.enqueue(i)
    for i in range(5):
        print(q.dequeue())

if __name__ == "__main__":
    test()