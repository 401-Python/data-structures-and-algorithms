def insert_shift_array(lst, val):
  middle = len(lst) // 2
  if len(lst) % 2 != 0:
    middle +=1
  lst[middle:middle] = [val]
  return lst

insert_shift_array([1, 2, 4], 3)