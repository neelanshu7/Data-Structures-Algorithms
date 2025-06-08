# Linked List
A Linked List is a linear data structure where elements (called nodes) are stored in a sequence, but unlike arrays, they are not stored in contiguous memory locations. Each node contains two parts:
	Data – the actual value or information.
	Pointer (Link) – a reference to the next node in the sequence.
Linked Lists are dynamic in nature, meaning they can grow or shrink in size during runtime, making them more flexible than arrays for insertion and deletion operations.

# Types of Linked Lists
## 1. Singly Linked List (SLL)
In a Singly Linked List, each node contains:
	Data
	Pointer to the next node

The last node points to null (or None in Python), marking the end of the list.
**Advantages:**
	Easy to implement
	Efficient insertion/deletion at the beginning
**Disadvantages:**
	No backward traversal
	Slower access to specific elements (no indexing)

## 2. Doubly Linked List (DLL)
A Doubly Linked List allows both forward and backward traversal. Each node has:
	Data
	Pointer to the next node
 	Pointer to the previous node

**Advantages:**
	Can be traversed in both directions
	Easier deletion from the end or middle
**Disadvantages:**
	More memory usage due to extra pointer
	Slightly complex to implement
