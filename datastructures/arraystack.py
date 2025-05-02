import os

from datastructures.array import Array, T
from datastructures.istack import IStack

class ArrayStack(IStack[T]):
    ''' ArrayStack class that implements the IStack interface. The ArrayStack is a 
        fixed-size stack that uses an Array to store the items.'''
    
    def __init__(self, max_size: int = 0, data_type=object) -> None:
        ''' Constructor to initialize the stack 
        
            Arguments: 
                max_size: int -- The maximum size of the stack. 
                data_type: type -- The data type of the stack.       
        '''
        self.max_size = max_size
        self.stack = [None] * max_size
        self._top = -1

    def push(self, item: T) -> None:
        if self.full:
            raise IndexError
        self._top += 1
        self.stack[self._top] = item

    def pop(self) -> T:
       if self.empty:
           raise IndexError
       item = self.stack[self._top]
       self.stack[self._top] = None
       self._top -= 1
       return item

    def clear(self) -> None:
       self.stack = [None] * self.max_size
       self._top = -1

    @property
    def peek(self) -> T:
       if self.empty:
           raise IndexError
       return self.stack[self._top]

    @property
    def maxsize(self) -> int:
        ''' Returns the maximum size of the stack. 
        
            Returns:
                int: The maximum size of the stack.
        '''
        return self.max_size
        
    @property
    def full(self) -> bool:
        ''' Returns True if the stack is full, False otherwise. 
        
            Returns:
                bool: True if the stack is full, False otherwise.
        '''
        return self._top == self.max_size - 1

    @property
    def empty(self) -> bool:
        return self._top == -1
    
    def __eq__(self, other: object) -> bool:
       if not isinstance(other, ArrayStack):
           return False
       if self._top != other._top:
           return False
       return self.stack[:self._top + 1] == other.stack[:other._top + 1]

    def __len__(self) -> int:
       return self._top + 1
    
    def __contains__(self, item: T) -> bool:
       return item in self.stack[:self._top + 1]

    def __str__(self) -> str:
        return str([self.stack[i] for i in range(self._top + 1)])
    
    def __repr__(self) -> str:
        return f"ArrayStack({self.maxsize}): items: {str(self)}"
    
if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')

