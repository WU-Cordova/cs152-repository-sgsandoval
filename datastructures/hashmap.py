import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT, VT]]] = Array(number_of_buckets)
        for i in range(number_of_buckets):
            self._buckets[i] = LinkedList()
        self._count: int = 0
        self._load_factor_threshold: float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def _get_bucket_index(self, key: KT, bucket_size: int) -> int:
        return self._hash_function(key) % bucket_size

    def __getitem__(self, key: KT) -> VT:
        bucket_index = self._get_bucket_index(key, len(self._buckets))
        for k, v in self._buckets[bucket_index]:
            if k == key:
                return v
        raise KeyError

    def __setitem__(self, key: KT, value: VT) -> None:        
        if self._count / len(self._buckets) >= self._load_factor_threshold:
            self._resize()
        bucket_index = self._get_bucket_index(key, len(self._buckets))
        bucket = self._buckets[bucket_index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._count += 1

    def _resize(self) -> None:
        old_buckets = self._buckets
        new_capacity = len(old_buckets) * 2
        self._buckets = Array(new_capacity)
        for i in range(new_capacity):
            self._buckets[i] = LinkedList()
        old_count = self._count
        self._count = 0
        for bucket in old_buckets:
            for k, v in bucket:
                self[k] = v
        assert self._count == old_count

    def keys(self) -> Iterator[KT]:
        for bucket in self._buckets:
            for k, _ in bucket:
                yield k
    
    def values(self) -> Iterator[VT]:
        for bucket in self._buckets:
            for _, v in bucket:
                yield v

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket in self._buckets:
            for pair in bucket:
                yield pair
            
    def __delitem__(self, key: KT) -> None:
        bucket_index = self._get_bucket_index(key, len(self._buckets))
        bucket = self._buckets[bucket_index]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._count -= 1
                return
        raise KeyError
    
    def __contains__(self, key: KT) -> bool:
        bucket_index = self._get_bucket_index(key, len(self._buckets))
        for k, _ in self._buckets[bucket_index]:
            if k == key:
                return True
        return False


    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        return self.keys()
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            return False
        if len(self) != len(other):
            return False
        for key, value in self.items():
            if key not in other or other[key] != value:
                return False
        return True

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self.items()) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)