

def insertion_sort(ints):
  '''
  Traverse from 1 to len(ints)
  J starts one spot behind i (i-1)
  While j >=0 and the value at i
  is less than the value at j,
  the value at j+1 gets reassigned to the
  value at j, and j+1 becomes the value at i
  '''
  for i in range(1, len(ints)):
    temp = ints[i]
    j = i-1
    while j >= 0 and temp < ints[j]:
      ints[j + 1] = ints[j]
      j -=1
    ints[j + 1] = temp
  return ints


if __name__ == "__main__":
  a = [5, 2, 32, 4, 17, 1, 7]
  print(insertion_sort(a))
    