# Linked List
A Linked List is a linear data structure where elements (called nodes) are stored in a sequence, but unlike arrays, they are not stored in contiguous memory locations. Each node contains two parts:
	Data – the actual value or information.<br>
	Pointer (Link) – a reference to the next node in the sequence.<br>
Linked Lists are dynamic in nature, meaning they can grow or shrink in size during runtime, making them more flexible than arrays for insertion and deletion operations.

# Types of Linked Lists
## 1. Singly Linked List (SLL)
In a Singly Linked List, each node contains:<br>
	Data<br>
	Pointer to the next node<br>

The last node points to null (or None in Python), marking the end of the list.
**Advantages:**
	Easy to implement<br>
	Efficient insertion/deletion at the beginning<br>
**Disadvantages:**
	No backward traversal<br>
	Slower access to specific elements (no indexing)<br>

## 2. Doubly Linked List (DLL)
A Doubly Linked List allows both forward and backward traversal. Each node has:<br>
	Data<br>
	Pointer to the next node<br>
 	Pointer to the previous node

**Advantages:**
	Can be traversed in both directions<br>
	Easier deletion from the end or middle<br>
**Disadvantages:**
	More memory usage due to extra pointer<br>
	Slightly complex to implement

## 3. Circular Linked List (CLL)
In a Circular Linked List, the last node points back to the first node. It can be<br>
	Singly Circular Linked List: Only next pointer loops to the head.<br>
	Doubly Circular Linked List: Both next and prev form a circle.
 
 **Advantages:**
	Can go around the list endlessly<br>
	Useful in circular task scheduling
**Disadvantages:**
	Requires careful traversal to avoid infinite loops
