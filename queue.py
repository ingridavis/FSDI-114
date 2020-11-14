class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items ==[]
    #if queue is empty
    def enqueue(self, item):
        self.items.insert(0, item)

    #new items
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    #size of list

def balance_check(string):
    if len(string)%2 != 0:
        return False

    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}') ])
    stack = []
    for paren in string:
        print("paren: %s" % paren)
        if paren in opening:
            stack.append(paren)
            print("paren is found in opening; stack is %s" % stack)
        else:
            if len(stack)==0:
                print("The stack's length is 0, so this is a fail condition")
                return False
            last_open = stack.pop()
            print("last open(last item from stack): %s" % last_open)
            temp_tuple =(last_open, paren)
            if (last_open, paren) not in matches:
                return False
    return len(stack) == 0
              
