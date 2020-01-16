
`arr = [1, 8, 3, 9, 4, 5, 7]`
Indexes:  0   1   2   3   4   5   6 

low = 0,   
high =  6,  
pivot = arr[h] = 7   
###i = -1 

Traverse from `j = low` to `high-1`    
j = 0 : Since `arr[j] <= pivot`, do i++ and swap(arr[i], arr[j])
i = 0 

`arr = [1, 8, 3, 9, 4, 5, 7]`
i and j are the same so no change  

j = 1 : Since `arr[j] > pivot`, do nothing  
No change in i and arr[]

j = 2 : Since `arr[j] <= pivot`, iterate i and swap(arr[i], arr[j])  
i = 1  
`arr = [1, 3, 8, 9, 4, 5, 7]`  We swap 8 and 3

j = 3 : Since `arr[j] > pivot`, do nothing  
No change in i and arr[]

j = 4 : Since `arr[j] <= pivot`, iterate i and swap(arr[i], arr[j])  
i = 2  

`arr = [1, 3, 4, 9, 8, 5, 7]` 8 and 4 swapped
j = 5 : Since `arr[j] <= pivot`, iterate and swap arr[i] with arr[j] 
i = 3   
`arr = [1, 3, 4, 5, 8, 9, 7]` 9 and 5 Swapped 

`j == high-1`, breaking the loop  
Finally we place pivot at correct position by swapping  
arr[i+1] and arr[high] (or pivot) 

`arr = [1, 3, 4, 5, 7, 9, 8]` 8 and 7 Swapped 

