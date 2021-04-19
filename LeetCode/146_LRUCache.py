"""
Data structure design problem.
"""
from collections import OrderedDict
"""
OrderedDict methods:
1. .popitem(last=True): pop the last key, value pair. (LIFO)
2. .move_to_end(key, last=True): move the key to the last.
"""


class LRUCache(OrderedDict):
    """
    At the end of `self` dict, is the most recently used key, value pair.
    At the beginning of the `self` dict, is the LRU key, value pair.
    Space complexity: O(n)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        Time complexity: O(1)
        """
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        """
        Time complexity: O(1)
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
