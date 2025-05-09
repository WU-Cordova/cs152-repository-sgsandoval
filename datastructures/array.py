# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import copy
import os
from typing import Any, Iterator, overload
import numpy as np



from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T] | int = [], data_type: type = object) -> None:
        if isinstance(starting_sequence, int):
            self.__logical_size = 0
            self.__physical_size = starting_sequence
            self.__data_type = data_type
            self.__elements = np.empty(self.__physical_size, dtype=self.__data_type)
        elif isinstance(starting_sequence, Sequence):
            self.__logical_size = len(starting_sequence)
            self.__physical_size = self.__logical_size
            self.__data_type = data_type
            self.__elements = np.empty(self.__logical_size, dtype=self.__data_type)
            for i in range(self.__logical_size):
                self.__elements[i] = copy.deepcopy(starting_sequence[i])
        else:
            raise ValueError("starting_sequence must be a valid sequence or integer")


    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:
        if isinstance(index, slice):
            return Array(starting_sequence=self.__elements[index].tolist())
        elif isinstance(index, int):
            if index < 0 or index >= self.__logical_size:
                raise IndexError("Index out of bounds")
            return self.__elements[index]
        raise TypeError("Invalid argument type")

    
    def __setitem__(self, index: int, item: T) -> None:
        self.__elements[index] = item

    def append(self, data: T) -> None:
        if self.__logical_size == self.__physical_size:
            self.__physical_size = max(1, self.__physical_size * 2)
            new_elements = np.empty(self.__physical_size, dtype = self.__data_type)
            new_elements[:self.__logical_size] = self.__elements
            self.__elements = new_elements

        self.__elements[self.__logical_size] = data
        self.__logical_size += 1

    def append_front(self, data: T) -> None:
        if self.__logical_size == self.__physical_size:
            self.__physical_size = max(1, self.__physical_size * 2)
            new_elements = np.empty(self.__physical_size, dtype=self.__data_type)
            new_elements[1:self.__logical_size + 1] = self.__elements[:self.__logical_size]
            self.__elements = new_elements
        else:
            self.__elements[1:self.__logical_size + 1] = self.__elements[:self.__logical_size]
        
        self.__elements[0] = data
        self.__logical_size += 1

    def pop(self) -> None:
        if self.__logical_size == 0:
            raise IndexError

        self.__logical_size -= 1

        if self.__logical_size > 0 and self.__logical_size <= self.__physical_size // 4:
            self.__physical_size = self.__physical_size // 2
            new_elements = np.empty(self.__physical_size, dtype=self.__data_type)
            new_elements[:self.__logical_size] = self.__elements[:self.__logical_size]
            self.__elements = new_elements
    
    def pop_front(self) -> None:
        if self.__logical_size == 0:
            raise IndexError
        
        self.__elements[:self.__logical_size - 1] = self.__elements[1:self.__logical_size]
        self.__logical_size -= 1
        
        if self.__logical_size > 0 and self.__logical_size <= self.__physical_size // 4:
            self.__physical_size = self.__physical_size // 2
            new_elements = np.empty(self.__physical_size, dtype = self.__data_type)
            new_elements[:self.__logical_size] = self.__elements[:self.__logical_size]
            self.__elements = new_elements

    def __len__(self) -> int: 
        return self.__logical_size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False
        
        if self.__logical_size != other.__logical_size:
            return False
        
        return np.array_equal(self.__elements[:self.__logical_size], other.__elements[:other.__logical_size])

    def __iter__(self) -> Iterator[T]:
        return iter(self.__elements[:self.__logical_size])

    def __reversed__(self) -> Iterator[T]:
        reversed_elements = np.flip(self.__elements)
        return iter(reversed_elements)

    def __delitem__(self, index: int) -> None:
       if not 0 <= index < self.__logical_size:
           raise IndexError
       
       self.__elements[index:self.__logical_size - 1] = self.__elements[index + 1:self.__logical_size]
       self.__logical_size -= 1

       if self.__logical_size > 0 and self.__logical_size <= self.__physical_size // 4:
           self.__physical_size //=2
           new_elements = np.empty(self.__physical_size, dtype=self.__data_type)
           new_elements[:self.__logical_size] = self.__elements[:self.__logical_size]
           self.__elements = new_elements

    def __contains__(self, item: Any) -> bool:
        return np.any(self.__elements[:self.__logical_size] == item)

    def clear(self) -> None:
        self.__logical_size = 0
        self.__elements = np.empty(self.__physical_size, dtype = self.__data_type)

    def __str__(self) -> str:
        return f'[{", ".join(str(item) for item in self.__elements[:self.__logical_size])}]'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {len(self.__items)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')