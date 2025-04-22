from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.head: Optional[LinkedList.Node] = None
        self.tail: Optional[LinkedList.Node] = None
        self.count: int = 0
        self.data_type: type = data_type
    
    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        linked_list = LinkedList(data_type)
        for item in sequence:
            linked_list.append(item)
        return linked_list

    def append(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError
        new_node = self.Node(data=item)
        if self.tail:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1

    def prepend(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError
        new_node = self.Node(data=item)
        if self.head:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
        self.count += 1

    def insert_before(self, target: T, item: T) -> None:
        if not isinstance(item, self.data_type) or not isinstance(target, self.data_type):
            raise TypeError
        current = self.head
        while current:
            if current.data == target:
                new_node = self.Node(data=type)
                new_node.next = current
                new_node.previous = current.previous
                if current.previous:
                    current.previous.next = new_node
                else:
                    self.head = new_node
                current.previous = new_node
                self.count += 1
                return
            current = current.next
        raise ValueError

    def insert_after(self, target: T, item: T) -> None:
        if not isinstance(item, self.data_type) or not isinstance(target, self.data_type):
            raise TypeError
        current = self.head
        while current:
            if current.data == target:
                new_node = self.Node(data=item)
                new_node.previous = current
                new_node.next = current.next
                if current.next:
                    current.next.previous = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                self.count += 1
                return
            current = current.next
        raise ValueError

    def remove(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError
        current = self.head
        while current:
            if current.data == item:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                self.count -= 1
                return
            current = current.next
        raise ValueError

    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError
        current = self.head
        while current:
            if current.data == item:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous
                self.count -= 1
            current = current.next

    def pop(self) -> T:
        if self.empty:
            raise IndexError
        item = self.tail.data
        self.remove(item)
        return item
    
    def pop_front(self) -> T:
        if self.empty:
            raise IndexError
        item = self.head.data
        self.remove(item)
        return item

    @property
    def front(self) -> T:
        if self.empty:
            raise IndexError
        return self.head.data

    @property
    def back(self) -> T:
        if self.empty:
            raise IndexError
        return self.tail.data

    @property
    def empty(self) -> bool:
        return self.count == 0

    def __len__(self) -> int:
        return self.count
    
    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def __contains__(self, item: T) -> bool:
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __iter__(self) -> ILinkedList[T]:
        self._iter_node = self.head
        return self
    
    def __next__(self) -> T:
        if self._iter_node is None:
            raise StopIteration
        data = self._iter_node.data
        self._iter_node = self._iter_node.next
        return data
    
    def __reversed__(self) -> ILinkedList[T]:
        reversed_list = LinkedList(self.data_type)
        current = self.tail
        while current:
            reversed_list.append(current.data)
            current = current.previous
        return reversed_list
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if len(self) != len(other):
            return False
        current_self = self.head
        current_other = other.head
        while current_self:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
