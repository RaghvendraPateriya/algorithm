"""
Implementing Python Dictionary using hash function without collision handling. 

"""

class HashTable:
  
  def __init__(self):
    self.MAX_SIZE = 100
    self.arr = [None] * self.MAX_SIZE
  
  def get_hash(self, key):
    h = 0
    for character in key:
      h += ord(character)
    return h % self.MAX_SIZE
  
  def __setitem__(self, key, val):
    index = self.get_hash(key)
    self.arr[index] = val

  def __getitem__(self, key):
    index = self.get_hash(key)
    return self.arr[index]
  
  def __delitem__(self, key):
    index = self.get_hash(key)
    self.arr[index] = None

# Driver Coded

if __name__ == "__main__":
    dictionary = HashTable()
    dictionary["age"] = 5 # Add value
    dictionary["name"] = "Raghu" # Add more value
    print(dictionary.arr) # See the Hash table
    print(dictionary["name"]) # print "Raghu"
    del dictionary['age'] # delete age
    print(dictionary.arr) # See the Hash table
