from __future__ import annotations
import os
from typing import Iterator, List, Sequence
import numpy as np

from datastructures.iarray import IArray
from datastructures.array import Array
from datastructures.iarray2d import IArray2D, T


class Array2D(IArray2D[T]):

    class Row(IArray2D.IRow[T]):
        def __init__(self, row_index: int, array: IArray, num_columns: int) -> None:
            self.row_index = row_index
            self.array = array
            self.num_columns = num_columns

        def map_index(self, row_index: int, col_index) -> int:
            return row_index * self.num_columns + col_index

        def __getitem__(self, column_index: int) -> T:
            if column_index < 0 or column_index >= self.num_columns:
                raise IndexError
            index: int = self.map_index(self.row_index, column_index)
            return self.array[index]

        def __setitem__(self, column_index: int, value: T) -> None:
            if column_index < 0 or column_index >= self.num_columns:
                raise IndexError
            index: int = self.map_index(self.row_index, column_index)
            self.array[index] = value
        
        def __iter__(self) -> Iterator[T]:
            for col in range(self.num_columns):
                yield self[col]
        def __reversed__(self) -> Iterator[T]:
            for col in range(self.num_columns -1, -1, -1):
                yield self[col]

        def __len__(self) -> int:
            return self.num_columns
        
        def __str__(self) -> str:
            return f"[{', '.join([str(self[column_index]) for column_index in range(self.num_columns)])}]"
        
        def __repr__(self) -> str:
            return f'Row {self.row_index}: [{", ".join([str(self[column_index]) for column_index in range(self.num_columns - 1)])}, {str(self[self.num_columns - 1])}]'


    def __init__(self, starting_sequence: Sequence[Sequence[T]]=[[]], data_type=object) -> None:
        self.data_type = data_type
        
        if not isinstance(starting_sequence) or not all(isinstance(row, Sequence) for row in starting_sequence):
            raise ValueError
        
        self.rows_len = len(starting_sequence)
        self.cols_len = len(starting_sequence[0] if self.rows_len > 0 else 0)

        if any(len(row) != self.cols_len for row in starting_sequence):
            raise ValueError
        
        py_list = [elem for row in starting_sequence for elem in row]
        self.elements2d = Array(starting_sequence=py_list, data_type = data_type)

    @staticmethod
    def empty(rows: int=0, cols: int=0, data_type: type=object) -> Array2D:
        pylist2d: List[List[T]] = [[data_type() for _ in range(cols)] for _ in range(rows)]
        return Array2D(starting_sequence=pylist2d, data_type=data_type)

    def __getitem__(self, row_index: int) -> Array2D.IRow[T]: 
        if row_index < 0 or row_index >= self.rows_len:
            raise IndexError
        return Array2D.Row(row_index, self.elements2d, self.cols_len)
    
    def __iter__(self) -> Iterator[Sequence[T]]: 
        for row in range(self.rows_len):
            yield self[row]

    def __reversed__(self):
        for row in range(self.rows_len -1, -1, -1):
            yield self[row]

    def __len__(self): 
        return self.rows_len
                                  
    def __str__(self) -> str: 
        return f'[{", ".join(f"{str(row)}" for row in self)}]'
    
    def __repr__(self) -> str: 
        return f'[{Array2D(rows={self.rows_len}, cols ={self.cols_len})}]'

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')