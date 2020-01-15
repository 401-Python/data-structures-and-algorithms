from merge_sort import merge_sort

def test_merge_sort():
  arr = [12, 11, 13, 5, 6, 7]
  assert merge_sort(arr) == [5, 6, 7, 11, 12, 13]