from typing import Iterable, Optional, TypeVar
from DataStructures.ibag import IBag, T
from collections import defaultdict

T = TypeVar("T")

class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.bag_dict = defaultdict(int)
        for iterable in items:
            for item in iterable:
                self.bag_dict[item] += 1


    def add(self, item: T) -> None:
        if item is None:
            raise TypeError
        self.bag_dict[item] += 1

    def remove(self, item: T) -> None:
        if item is None:
            raise ValueError
        if item in self.bag_dict:
            if self.bag_dict[item] > 1:
                self.bag_dict[item] -= 1
            else:
                del self.bag_dict[item]
        else:
            raise ValueError

    def count(self, item: T) -> int:
        if item is None:
            raise ValueError
        return self.bag_dict.get(item, 0)

    def __len__(self) -> int:
        return sum(self.bag_dict.values())

    def distinct_items(self) -> int:
        return set(self.bag_dict.keys())

    def __contains__(self, item: T) -> bool:
        if item is None:
            raise ValueError
        return item in self.bag_dict

    def clear(self) -> None:
        self.bag_dict.clear()