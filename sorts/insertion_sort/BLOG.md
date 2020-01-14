## Trace
ints: `[5, 2, 32, 4, 17]` 

Loop from 2nd element `i=1` to last element `len(ints)`:

### i = 1 [5, (2), 32, 4, 17] 
  * Since 2 is less than 5, move 5 and insert 2 before 5
  * `[2, 5, 32, 4, 17]`

### i = 2 [2, 5, (32), 4, 17]
  * Since all elements left of 32 are smaller, 32 doesn't remains where it is  

### i = 3 [2, 5, 32, (4), 17] 
  * 4 moves to index 1 and everything from 5 on moves 1 spot to the right (j + 1)
  * `[2, 4, 5, 32, 17]` 

### i = 4 [2, 4, 5, 32, (17)] 
  * 17 will move one spot to the left and 32 gets moved up 1 spot.
  * `[2, 4, 5, 17, 23]` 

