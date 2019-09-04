import math

def is_prime(integer):
    if integer < 2:
        return False
    if integer in [2,3]:
        return True
    if integer % 2 == 0:
        return False
    n = int(math.sqrt(integer))
    k = 3
    while k <= n:
        if integer % k == 0:
            return False
        k += 2
    return True

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.unhashables = [type(dict()), type(list()), type(set())]

    def hash_function(self, key):
        if type(key) == type(float()):
            return int(key) % self.size
        elif type(key) == type(int()):
            return key % self.size
        else:
            return len(key) % self.size

    def rehash(self, key):
        if type(key) == type(float()):
            return (int(key) + 3) % self.size
        elif type(key) == type(int()):
            return (key + 3) % self.size
        else:
            return (len(key) + 3) % self.size

    def resize(self):
        n = self.size
        self.size += 1
        while not is_prime(self.size):
            self.size += 1
        self.slots += ([None] * (self.size - n))
        self.data += ([None] * (self.size - n))

    def puts(self, key, value):
        if type(key) in self.unhashables:
            raise TypeError
        if None not in self.slots:
            self.resize()
        position = self.hash_function(key)
        if self.slots[position] == None:
            self.slots[position] = key
            self.data[position] = value
        elif self.slots[position] == key:
            self.data[position] = value
        else:
            new_position = self.rehash(key)
            while self.slots[new_position] is not None:
                new_position = self.rehash(new_position)
            if self.slots[new_position] == None:
                self.slots[new_position] = key
                self.data[new_position] = value

    def get(self, key):
        if key in self.slots and key is not None:
            position = self.hash_function(key)
            while self.slots[position] != key or self.data[position] == None:
                position = self.rehash(key)
            return self.data[position]
        return None

    def get_keys(self):
        return [key for key in self.slots if key is not None]

    def get_values(self):
        return [val for val in self.data if val is not None]

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.puts(key, value)

    def __str__(self):
        keys = self.get_keys()
        vals = self.get_values()
        result = "{"
        for i in range(len(keys)):
            if i == len(keys) - 1:
                pair = "{k}: {v}".format(k=keys[i], v=vals[i])
            else:
                pair = "{k}: {v}, ".format(k=keys[i], v=vals[i])
            result += pair
        result += "}"
        return result
