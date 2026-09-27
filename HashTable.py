class HashTable:
    
    def __init__(self):
        self.collection = {}

    def hash(self, value: str):
        total = 0
        for i in value:
            total = total + ord(i)
        return total 

    def add(self, k, v):
        hashed = self.hash(k)

        
        if not hashed in self.collection:
            self.collection[hashed] = {k:v}
        self.collection[hashed][k] = v

    def remove(self, k):
        hashed = self.hash(k)

        if hashed in self.collection and k in self.collection[hashed]:
            del self.collection[hashed][k]
        
    def lookup(self, k):
        hashed = self.hash(k)
        if hashed in self.collection and k in self.collection[hashed]:
            return self.collection[hashed][k]
    
        return None
        
