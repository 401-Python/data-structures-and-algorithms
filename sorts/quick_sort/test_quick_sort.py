from quick_sort import quick_sort

def test_quick_sort():
   arr = [8, 4, 3, 7, 1, 9]
   n = len(arr)
   quick_sort(arr, 0, n-1)
   assert arr == [1,3,4,7,8,9]

def test_few_uniques_quick_sort():
    lst = [5,12,7,5,5,7]
    quick_sort(lst, 0, 5)
    assert lst == [5, 5, 5, 7, 7, 12]