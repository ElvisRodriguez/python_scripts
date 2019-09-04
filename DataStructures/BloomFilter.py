"""
Q. What is a bloom filter?
A. Essentially a 'lightweight' version of a hash table with efficient insertions
   and lookups.

Q. What makes it different to a hash table?
A. It's more spacially efficient than a hash table at the cost of having 'false
   positives' for entry lookup.

Q. What is one use case for a bloom filter?
A. I want a data structure that allows for fast lookups and insertions, I care
   about how much space the data structure uses. I don't care if the data
   structure sometimes indicates an item is present when in fact it is not.

Q. One real-world example of bloom filter being useful?
A. Running a website that blocks certain IP addresses and does not mind if
   those addresses can occasionally access the website but does mind if
   'innocent' IP addresses cannot (more spacially efficient to store only
   blocked IP addresses versus unblocked ones).
"""
import pyhash


class BloomFilter:
    def __init__(self, max_size):
        # max size is approximately the maximum amount of insertions into the
        # bloom filter which is then used to calculate the bit vector size
        # that yields a low albeit nonzero chance of false positives.
        self.size = (max_size * 100) % (2 ** 60 - 1)
        self.bit_vector = [0] * self.size
        # Non cryptographic hash functions: (murmur, fnv).
        self.fnv = pyhash.fnv1_32()
        self.murmur = pyhash.murmur3_32()

    def insert(self, item):
        self.bit_vector[self.fnv(item) % self.size] = 1
        self.bit_vector[self.murmur(item) % self.size] = 1

    def not_in_bit_vector(self, item):
        # Will always be accurate if the item is actually not stored in the
        # bit vector. A check to see if it is would prove unreliable due
        # to the probabilistic nature of a bloom filter.
        if self.bit_vector[self.fnv(item) % self.size] == 0:
            return True
        elif self.bit_vector[self.murmur(item) % self.size] == 0:
            return True
        return False

    def number_of_items(self):
        # Returns the approximate amount of 'items' in the bit vector, the
        # probability of count being inaccurate grows slowly as the sample
        # size approaches 2^60.
        count = 0
        for bit in self.bit_vector:
            if bit:
                count += 1
        # Count is divided by the number of hash functions used by the bloom
        # filter.
        return count // 2
