import os
from DataStructures.istack import IStack
from typing import Generic

from DataStructures.linkedlist import LinkedList, T

class ListStack(IStack[T]):
    """
    ListStack (LinkedList-based Stack)

    """

    def __init__(self, data_type:object) -> None:
        self._list = LinkedList(data_type=data_type)
        self.size = 0

    def push(self, item: T):
        self._list.append(item)
        self.size += 1

    def pop(self) -> T:
        if self.empty:
            raise IndexError
        item = self._list.pop()
        self.size -= 1
        return item

    def peek(self) -> T:
        if self.empty:
            raise IndexError
        current = self._list.head
        while current.next:
            current = current.next
        return current.data

    @property
    def empty(self) -> bool:
        return self.size == 0

    def clear(self):
        self._list.clear()
        self.size = 0

    def __contains__(self, item: T) -> bool:
        current = self._list.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def __eq__(self, other) -> bool:
        if not isinstance(other, ListStack):
            return False
        if len(self) != len(other):
            return False
        current_self = self._list.head
        current_other = other._list.head
        while current_self and current_other:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

    def __len__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return str(self._list)

    def __repr__(self) -> str:
        return f"ListStack({repr(self._list)})"

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
