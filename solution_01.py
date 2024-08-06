
from typing import TypeVar, List

T = TypeVar("T") 
Node = TypeVar("Node")  
DLL = TypeVar("DLL")

class Node:
    """
    Implementation of a doubly linked list node.
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.
        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.
        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
            if node is self.head:
                break
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    def __eq__(self, other: DLL) -> bool:
        """
        :param other: compares equality with this List
        :return: True if equal otherwise False
        """
        cur_node = self.head
        other_node = other.head
        while True:
            if cur_node != other_node:
                return False
            if cur_node is None and other_node is None:
                return True
            if cur_node is None or other_node is None:
                return False
            cur_node = cur_node.next
            other_node = other_node.next
            if cur_node is self.head and other_node is other.head:
                return True
            if cur_node is self.head or other_node is other.head:
                return False


    def empty(self) -> bool:
        """
        Checks if the DLL is empty.

        :return: True if the DLL is empty, False otherwise.
        """
        return self.size == 0
        pass

    def push(self, val: T, back: bool = True) -> None:
        """
        Inserts a new value into the DLL.

        :param val: The value to insert.
        :param back: If True, the value is inserted at the end; if False, at the beginning.
        :return: None
        """
        new_node = Node(val)
        if self.head is None:  # empty list
            self.head = self.tail = new_node
        elif back:  # appending the new node to the back
            new_node.prev = self.tail
            new_node.next = None
            if self.tail:
                self.tail.next = new_node
            self.tail = new_node
        else:  # appending the new node to the front
            new_node.next = self.head
            new_node.prev = None
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        self.size += 1
        pass

    def pop(self, back: bool = True) -> None:
        """
        Removes a value from the DLL.

        :param back: If True, removes from the end; if False, removes from the beginning.
        :return: None
        """
        if self.head is None:
            pass
        elif back:
            if self.tail.prev:
                p_node = self.tail.prev
                p_node.next = None
                self.tail = p_node
            else:
                self.head = self.tail = None
        else:
            if self.head.next:
                n_node = self.head.next
                n_node.prev = None
                self.head = n_node
            else:
                self.head = self.tail = None
        self.size -= 1
        pass

    def list_to_dll(self, source: List[T]) -> None:
        """
        Converts a list to a DLL.

        :param source: The list to convert.
        :return: None
        """
        self.head = self.tail = None
        self.size = 0

        for i in source:
            new_node = Node(i)
            if self.head is None:
                self.head = self.tail = new_node
            else:
                new_node.prev = self.tail
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
        self.size = len(source)
        pass

    def dll_to_list(self) -> List[T]:
        """
        Converts the DLL to a list.
        :return: A list containing all the values from the DLL.
        """
        new_list = []
        if self.head is None:
            return new_list
        else:
            curr = self.head
            while curr:
                new_list.append(curr.value)
                curr = curr.next
            return new_list
        pass

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Finds nodes with a specific value.

        :param val: The value to find.
        :param find_first: If True, returns the first found node only.
        :return: A list of nodes with the specified value.
        """
        curr = self.head
        new_list = []
        while curr:
            if curr.value == val:
                new_list.append(curr)
                if find_first:
                    break
            curr = curr.next
        return new_list
        pass

    def find(self, val: T) -> Node:
        """
        Find the first node with a specific value.

        :param val: The value to be found.
        :return: The first node with the specified value, or None if not found.
        """
        found_nodes = self._find_nodes(val, True)
        if found_nodes:
            return found_nodes[0]
        else:
            return None
        pass

    def find_all(self, val: T) -> List[Node]:
        """
        Find all nodes with a specific value.

        :param val: The value to be found.
        :return: A list of nodes with the specified value.
        """
        all_found_nodes = self._find_nodes(val, False)
        if all_found_nodes:
            return all_found_nodes
        else:
            return []
        pass

    def _remove_node(self, to_remove: Node) -> None:
        """
        Remove a specific node from the doubly linked list.

        :param to_remove: The node to be removed.
        :return: None.
        """
        if to_remove is None:
            pass

        if to_remove.prev is not None:
            to_remove.prev.next = to_remove.next

        else:
            self.head = to_remove.next

        if to_remove.next is not None:
            to_remove.next.prev = to_remove.prev
        else:
            self.tail = to_remove.prev

        self.size -= 1
        pass

    def remove(self, val: T) -> bool:
        """
        Remove the first node with a specific value.

        :param val: The value to be removed.
        :return: True if a node was removed, False otherwise.
        """
        curr = self.head
        while curr:
            if curr.value == val:
                self._remove_node(curr)
                return True
            curr = curr.next
        return False
        pass

    def remove_all(self, val: T) -> int:
        """
        Remove all nodes with a specific value.

        :param val: The value to be removed.
        :return: The number of nodes removed.
        """
        curr = self.head
        c = 0
        while curr:
            if curr.value == val:
                self._remove_node(curr)
                c += 1
            curr = curr.next
        return c
        pass

    def reverse(self) -> None:
        """
        Reverse the doubly linked list.
        :return: None.
        """
        curr = self.head
        self.head, self.tail = self.tail, self.head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev
        pass


def dream_escaper(dll: DLL) -> DLL:
    """
    Flatten a doubly linked list with child pointers into a single-level doubly linked list.
    :param dll: The doubly linked list to be flattened.
    :return: The flattened doubly linked list.
    """
    if dll.head is None:
        return dll

    curr = dll.head
    while curr:
        if curr.child:
            child_curr = curr.child
            while child_curr.next:
                child_curr = child_curr.next
            child_curr.next = curr.next
            if curr.next:
                curr.next.prev = child_curr
            else:
                dll.tail = child_curr
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None

        curr = curr.next

    return dll
    pass
