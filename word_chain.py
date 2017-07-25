input = ["ant", "tea", "peas", "sugar", "rice", "soup", "eat"]

"""
 [
 ['ant', 'tea'],
 ['tea', 'ant', 'tea'],
 ['peas', 'sugar', 'rice', 'eat'], 
 ['sugar', 'rice', 'eat'],
 ['rice', 'eat'],
 ['soup', 'peas', 'sugar', 'rice', 'eat'],
 ['eat', 'tea']]
"""

def find_next_word(last_char, input, chain):
  next = None
  for i in input:
    if last_char == i[0]:
       if i in chain:
          continue
       return i

def get_elem_count(word_chain):
  count_dict = {}
  for chain in word_chain:
    count_dict[len(chain)] = chain
  return count_dict
      
def word_chain(input):
  word_chain = []

  for i in input:
    word = i
    last_char = word[len(word)-1]
    chain = [word]
    while True:
      next = find_next_word(last_char, input, chain)
      if next:
        chain.append(next)
        last_char = next[len(next)-1]
        continue 
      else:
         word_chain.append(chain)
         break 
  count_dict = get_elem_count(word_chain)
  print count_dict[sorted(count_dict, reverse=True)[0]]
word_chain(input)
