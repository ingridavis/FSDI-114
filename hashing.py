class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def put(self, key, data):
     # get the hash value
     hashvalue = self.hashfunction(key, len(self.slots))

     # if slot is empty

    if self.slots[hashvalue] == None:
         self.slots[hashvalue] = key
         self.data[hashvalue] = data
    
    else:
        if self.slots[hashvalue] ==key:
             self.data[hashvalue] = data
        else:
            nextslot = self.rehash(hashvalue, len(self, slots))

            while self.slots[nextslot] != None and self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot, len(self.slots))
            
            if self.slots[nextslot] == None:
                self.slots[nextslot] = key 
                self.slots[nextslot] = data 
            else:
                self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):

        return(oldhash +1)%size

    def get(self, key):
        # getting items given a key
        # set up variables for our search
        startslot = self.hashfunction(key, ken(self, slots))
        data = None
        stop = False
        found = False
        position = startslot

    # until we discern that its not empty or found 
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = true
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data
    # sepcial methods for use with python indexing
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key,data)


    if __name__ == "__main__":
        print(self,(11))