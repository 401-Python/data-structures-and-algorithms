from array_binary_search import binary_search_modified

test_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(test_arr) -1
def test_binary_search_happy_right():
  actual = binary_search_modified(test_arr, 0, length, 6)
  expected = 5
  assert actual == expected

def test_binary_search_happy_left():
  actual = binary_search_modified(test_arr, 0, length, 2)
  expected = 1
  assert actual == expected

def test_binary_search_not_found():
  actual = binary_search_modified(test_arr, 0, length,  32)
  expected = -1
  assert actual == expected