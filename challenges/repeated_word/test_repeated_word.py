from repeated_word import repeated_word, HashTable, LinkedList

def test_repeat_word():
  summer = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York"
  assert repeated_word(summer) == 'summer'

def test_no_repeat():
  no_repeat = 'I went to the store and bought some eggs. Unfortunately they were stolen by a breakfast thief.'
  assert repeated_word(no_repeat) == None