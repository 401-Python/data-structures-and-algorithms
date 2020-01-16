
def partition(arr,low,high): 
    i = ( low-1 )       
    pivot = arr[high]
  # block of code in for loop found on geeks for geeks by Mohit Kumra
    for j in range(low , high): 

        if   arr[j] < pivot: 
        
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
   
def quick_sort(arr,low,high): 
    if low < high: 
        p = partition(arr,low,high) 
  
        quick_sort(arr, low, p-1) 
        quick_sort(arr, p+1, high) 

if __name__ == "__main__":
    arr = [8, 4, 3, 7, 1, 9]
    n = len(arr)
    quick_sort(arr, 0, n-1)
    print(arr)
  