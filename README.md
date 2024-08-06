# Linked_Lists

## Project Overview

This project provides an implementation of a doubly linked list (DLL) in Python. It includes basic operations such as insertion, deletion, searching, and list conversion. Additionally, it includes a function to flatten a DLL with child pointers into a single-level DLL.

## Installation

No specific installation is required. Just clone the repository and run the `solution.py` file.

## Usage

### Class: Node

A node in the doubly linked list.

#### Attributes

- `value`: The value held by the node.
- `next`: Reference to the next node in the linked list.
- `prev`: Reference to the previous node in the linked list.
- `child`: Reference to the child node (used for the application problem).

### Class: DLL

A doubly linked list without padding nodes.

#### Methods

- `empty() -> bool`: Check if the DLL is empty.
- `push(val: T, back: bool = True) -> None`: Insert a value into the DLL.
- `pop(back: bool = True) -> None`: Remove a value from the DLL.
- `list_to_dll(source: List[T]) -> None`: Convert a list to a DLL.
- `dll_to_list() -> List[T]`: Convert the DLL to a list.
- `find(val: T) -> Node`: Find the first node with a specific value.
- `find_all(val: T) -> List[Node]`: Find all nodes with a specific value.
- `remove(val: T) -> bool`: Remove the first node with a specific value.
- `remove_all(val: T) -> int`: Remove all nodes with a specific value.
- `reverse() -> None`: Reverse the DLL.

### Function: dream_escaper

- `dream_escaper(dll: DLL) -> DLL`: Flatten a DLL with child pointers into a single-level DLL.

## Example

```python
dll = DLL()
dll.push(1)
dll.push(2)
dll.push(3, back=False)
print(dll)  # Output: Node(3) <-> Node(1) <-> Node(2)
dll.pop()
print(dll)  # Output: Node(3) <-> Node(1)
