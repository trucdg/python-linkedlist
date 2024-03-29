# Linked List in Python
## 👉 What is a Linked List?
- Linked list is a linear data structure.
- Elements in a linked list are stored in nodes.
- Each node in a singly linked list contains: 
  - a data value, and 
  - a pointer to the next node.

## 👉 Pros and Cons of a Linked list
### ✅ PROS:
- Easy to insert and delete (O(1) at the start of the list)
- Doesn't need to reorganize or shift data when insert/ delete in the middle of the list
- Doesn't require fixed/ initial memory allocations like arrays or lists

### ❎ CONS:
- Require more memory since we need to store pointers to nodes
- No Random access (like arrays)

## ⏰Time Complexity:

| Operation | Best Case | Worst Case |
| --- | --- | --- |
| Insert | O(1) | O(n) |
| Delete | O(1) | O(n) |
| Search | O(1) | O(n) |
- Best Case: when operating **_at the beginning of the list_**
- Worst Case: when operating **_at the end of the list_**

### The following are the methods implemented:
1. append(new_node) - append the new node to the end of the list
2. delete(val) - delete the first node with the given value 
3. insert(new_node, position) - insert a new node at the given position, assuming the first position is 1
4. print() - print the string representing the linked list

## Resources:
- [Two Pointers Technique in LinkedList](https://github.com/trucdg/linked-list-two-pointers)

