def binary_search(arr, val):
  left = 0
  right = len(arr)

  while left <= right:
    mid = (left + right) //2
    if arr[mid] == val:
      print(mid)
      return mid
    elif arr[mid] < val:
      left = mid
    else:
      right = mid
  print('no dice')
  return -1

# binary_search([1, 2, 3, 4, 5, 6, 7, 8], 9)

def binary_search_modified(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)//2; 
          
        if arr[mid] == x: 
            return mid 
  
        elif arr[mid] < x: 
            l = mid + 1
  
        else: 
            r = mid - 1
      
    return -1
  
  