def reverse_array(lst):
  newLst = []
  count = len(lst) -1
  while count >= 0:
    newLst.append(lst[count])
    count -= 1
  return newLst

reverse_array([4, 3, 2, 1])