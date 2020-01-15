## Trace
ints: `[5, 2, 32, 4, 17, 1, 18, 12]` 


Split `ints` into 2 halves: L and R  

`L [5, 2, 32, 4]`   
`R [17, 1, 18, 12]`


Call mergesort on L, which will continue to split the lists in half until only 1 element remains  
  `[5, 2, 32, 4]`  
  `[5, 2,]`  
  `[5], [2]`  

Once the left most pair has been split, stitch back together in order.
  `[5], [2]` becomes `[2, 5]`

Now the same process repeats for the right half of L, not to be confused with R
`[32, 4]`
`[32], [4]` becomes `[4, 32]`

Stitch L backtogether in order
  `[2, 4, 5, 32]`

Repeat the entire process for R `[17, 1, 18, 12]`  

`[17, 1, 18, 12]`  

`[17, 1] `  

`[17], [1]` becomes `[1, 17]`  

`[18, 12]`  
`[18], [12]` becomes `[12, 18]`

Merge R back together in order
  `[1, 12, 17, 18]`

Merge L `[2, 4, 5, 32]` and R `[1, 12, 17, 18]` to get  
 `[1, 2, 4, 5, 12, 17, 18, 32]`

