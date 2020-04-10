# Least Recently Used Cache

## Problem

We have briefly discussed caching as part of a practice problem while studying hash maps.

The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. For the current problem, consider both get and set operations as an use operation.

Your job is to use an appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5

## Requirements

Python version 3.6 and above

## Solution

The solution uses 2 types of data structures to implement the LRU cache. They are stored as references in the class and contain other variables to provide efficient access

1. cache - This is a Python dict that stores the values by using a hash of the key supplied. This allows O(1) for searching, adding or deleting of the values by keys.
2. tail, head - These are the references to the head and tail Nodes which is a doubly linked list that performs the behavior of a queue. The queue allows the First In First Out (FIFO), this allows us to add to the tail of the queue for the most currently access (get or set) node and remove the least recent access (get or set) node from the head of the queue in O(1). The queue is also implemented as a doubly linked list to allow accessing (get or set) a node in the middle of the queue to move the node to the tail in O(1).
