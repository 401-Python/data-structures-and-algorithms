

def left_join(map_a, map_b):
  '''
  This function takes in 2 hash maps and performs
  a simple left join based on if the keys
  If a key is present in both maps, we left join
  that keys value with our key, value pair from 
  the first map

  '''
  output = []

  for word in map_a:
    if map_b.__contains__(word):
       antonym = map_b.get(word)
       synonym = map_a[word]
       print(map_a[word] + 'test')
       output.append([word, synonym, antonym])
  
  print(output)
  return output


if __name__ == "__main__":
    lst1 = ['fond', 'wrath', 'diligent', 'outfit', 'guide']
    lst2 = ['enamored', 'anger', 'employed', 'garb', 'usher']
    lst3 = ['fond', 'wrath', 'diligent', 'guide', 'flow']
    lst4 = ['averse', 'delight', 'idle', 'follow','jam']

    map_a = dict(zip(lst1, lst2))

    map_b = dict(zip(lst3, lst4))

    left_join(map_a, map_b)