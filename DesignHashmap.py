class MyHashMap:

    def __init__(self):
        self.my_map = {}

    def put(self, key, value):
        self.my_map[key] = value

    def get(self, key):
        if key in self.my_map:
            return self.my_map[key]
        else:
            return -1

    def remove(self, key):
        if key in self.my_map:
            self.my_map.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
