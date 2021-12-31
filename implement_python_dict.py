"""
Implementing Python Dictionary using hash function without collision handling. 

"""

class HashTable:
  
  def __init__(self):
    MAX_SIZE = 100
    self.arr = [None] * MAX_SIZE
  
  def get_hash(self, key):
    h = 0
    for character in key:
      h += ord(character)
    return h % MAX_SIZE
  
  def __setitem__(self, key, val):
    index = get_hash(key)
    self.arr[index] = val

  def __getitem__(self, key):
    index = get_hash(key)
    return self.arr[index]
  
  def __delitem__(self, key):
    index = get_hash(key)
    self.arr[index] = None
    
    
