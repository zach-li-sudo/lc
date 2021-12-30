# sol 1: two arrays: Not acceptable
# class MyHashMap:
#     def __init__(self):
#         self.keys = []
#         self.values = []
        
#     def put(self, key: int, value: int) -> None:
#         if key not in self.keys:
#             self.keys.append(key)
#             self.values.append(value)
#         else:
#             index = self.keys.index(key)
#             self.values[index] = value

#     def get(self, key: int) -> int:
#         if key not in self.keys:
#             return -1
#         else:
#             index = self.keys.index(key)
#             return self.values[index]

#     def remove(self, key: int) -> None:
#         if key not in self.keys:
#             pass
#         else:
#             index = self.keys.index(key)
#             self.keys.pop(index)
#             self.values.pop(index)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)