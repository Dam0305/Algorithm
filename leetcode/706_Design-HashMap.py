class MyHashMap(object):

    def __init__(self):
        self.hash_map = dict()

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        self.hash_map[key] = value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.hash_map[key] if key in self.hash_map.keys() else -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hash_map.keys():
            self.hash_map.pop(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)