from array_shift import insert_shift_array

def test_insert_shift_even():
  actual = insert_shift_array([1, 2, 4, 5], 3)
  expected = [1, 2, 3, 4, 5]
  assert actual == expected


def test_insert_shift_odd():
  actual = insert_shift_array([1, 2, 3, 5, 6], 4)
  expected = [1, 2, 3, 4, 5, 6]
  assert actual == expected