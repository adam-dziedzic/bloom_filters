# Python 3 program to build Bloom Filter
# Install mmh3 and bitarray 3rd party module first
# pip install mmh3
# pip install bitarray
import math
import mmh3
import numpy as np
from bitarray import bitarray


class BloomFilter(object):
    """
    Class for Bloom Filters.
    """

    def __init__(self, items_count, fp_prob):
        """
        items_count : int
            Number of items expected to be stored in bloom filter
        fp_prob : float
            False Positive probability in decimal
        """
        # False possible probability in decimal
        self.fp_prob = fp_prob

        # Size of bit array to use
        self.size = self.get_size(items_count, fp_prob)

        # number of hash functions to use
        self.hash_count = self.get_hash_count(self.size, items_count)

        # Bit array of given size
        self.bit_array = bitarray(self.size)

        # initialize all bits as 0
        self.bit_array.setall(0)

    def hash(self, item: str, offset: int):
        """
        Crate a hash value for the item.

        :param item: string to be hashed
        :param offset: seed for the hash function
        :return: hash value of item
        """
        ints = [ord(c) for c in item]
        sum = np.sum(ints) + offset
        return sum % self.size

    def add(self, item):
        """
        Add an item in the filter
        """
        for i in range(self.hash_count):
            # create digest for given item.
            # i work as seed to mmh3.hash() function
            # With different seed, digest created is different
            digest = mmh3.hash(item, i) % self.size

            # set the bit True in bit_array
            self.bit_array[digest] = True

    def check(self, item):
        """
        Check for existence of an item in filter
        """
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                # if any of the bits is False then, it is not present in filter
                # else there is a probability that it present.
                return False
        return True

    @classmethod
    def get_size(self, items_count: int, p: float):
        """
        Return the size of bit array using the following formula:

        size = -(items_count * lg(p)) / (lg(2)^2)

        items_count : int
            number of items expected to be stored in filter
        p : float
            False Positive probability in decimal
        """
        size = (1 / math.log(2)) * math.log(1 / p, 2) * items_count
        return int(size)

    @classmethod
    def get_hash_count(self, n, items_count):
        """
        Return the hash function(k) to be used using
        following formula:

        k = (m/items_count) * lg(2)

        n : int
            size of bit array
        items_count : int
            number of items expected to be stored in filter
        """
        b = n / items_count
        k = math.log(2) * b
        return int(k)
