from quick_sort import quick_sort

def test_quick_sort():
   arr = [8, 4, 3, 7, 1, 9]
   n = len(arr)
   quick_sort(arr, 0, n-1)
   assert arr == [1,3,4,7,8,9]