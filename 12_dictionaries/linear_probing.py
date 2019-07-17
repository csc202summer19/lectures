class Dictionary:
    """ An unordered collection of key-value pairs """

    # NOTE: Use a prime capacity to mitigate collisions.
    def __init__(self, capacity = 17):
        # The backing array:
        self.array = [None] * capacity
        # The length of the backing array:
        self.capacity = capacity
        # The number of occupied spots in the array:
        self.occupied = 0
        # The number of key-value pairs:
        self.size = 0


def hash(key):
    """ Hashes a string key; transforms dictionary key into an array index. """
    # NOTE: Don't use more than a constant number of chars to keep this O(1).
    return sum([ord(c) for c in key[:21]])


# NOTE: This would have to happen in every single function anyways.
def _index(dct, key):
    """ Find the index of a key, if it exists. """
    # Get the raw hash value and mod it by the capacity.
    # While that index is already occupied by a different key, do:
    #     Increment the index by one modded by the capacity.
    # Return the resulting index -- either where the key is found or
    #  an empty spot.
    pass


def insert(dct, key, value):
    """ Insert a key-value pair into a dictionary. """
    # NOTE: For linear probing, the load factor should not exceed 0.7.
    # If ((occupied + 1) / capacity) >= 0.7, then:
    #     Expand the backing array (double and add one).
    #     For every meaningful key-value pair:
    #         Rehash the key and re-insert into the new array.
    #     Reset "occupied" to "size".
    #
    # Call "_index" to find the right index.
    # If the index was not occupied, then:
    #     NOTE: The hash value itself just tells you where to find things;
    #           it is never actually stored in the dictionary.
    #     Store a new key-value pair at that index.
    #     Increment the size and the occupied.
    # Else:
    #     Replace the value that was at that index. 
    pass


def get(dct, key):
    """ Get the value associated with a key. """
    # Call "_index" to find the right index.
    # If the index was not occupied, then:
    #     Raise an error.
    # Else:
    #     Return the value at that index.
    pass


def remove(dct, key):
    """ Remove a key-value pair from a dictionary. """
    # Call "_index" to find the right index.
    # If the index was not occupied, then:
    #     Raise an error.
    # Else:
    #     NOTE: We cannot actually remove the pair without destroying
    #           future probing.
    #     Set the key at that index to an impossible value.
    #     Decrement the size.
    pass
