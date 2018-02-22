# Topic covered in this recitation:

* Adjacency Matrix
    * Space needed: &Theta;(V<sup>2</sup>) bits
    * Compare to adjacency lists, which needs &Theta;(Ew) (python can initiate None for those
nodes without neigbors)
    * Adjacency list is a compact way to represent *sparse* graphs
    * Adjacency matrix is prefered when the graph is *dense*, i.e., E is close to V<sup>2</sup>
* Queue
    * Breadth first search (BFS) uses a queue to perform the search (FIFO, first in first out)
    * python provides builtin queue: collections.deque
    * deque is a doubly linked list, so it can do leftpop() and pop() in O(1) time, but need O(n)
time to access the items in the middle.
    * To abtain more randomly indexed item, use list instead.
