DFS algorithm
A standard DFS implementation puts each vertex of the graph into one a category of visited or not visited, with the
goal of marking each vertex visited, while avoiding cycles

Algorithm

Start by putting any one of the graph's vertices on top of a stack.
Take the top item of the stack and add it to the visited set.
Create a list of that vertex's adjacent nodes, and add the ones which aren't in the visited list to the top of stack.
Repeat until stack is empty