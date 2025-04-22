import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT, VT]]]
        self._count: int
        self._load_factor_threshold: float

    def _get_bucket_index(self, key: KT, bucket_size: int) -> int:
        bucket_index = self._buckets
        return bucket_index % bucket_size

    def __getitem__(self, key: KT) -> VT:
        for (k, v) in self._buckets[self._get_bucket_index(key, len(self._buckets))]:
            if k == key:
                return v
        raise KeyError

    def __setitem__(self, key: KT, value: VT) -> None:        
        raise NotImplementedError("HashMap.__setitem__() is not implemented yet.")

    def keys(self) -> Iterator[KT]:
        raise
    
    def values(self) -> Iterator[VT]:
        raise NotImplementedError("HashMap.values() is not implemented yet.")

    def items(self) -> Iterator[Tuple[KT, VT]]:
        raise NotImplementedError("HashMap.items() is not implemented yet.")
            
    def __delitem__(self, key: KT) -> None:
        raise NotImplementedError("HashMap.__delitem__() is not implemented yet.")
    
    def __contains__(self, key: KT) -> bool:
        bucket_index: int = self._get_bucket_index(key, len(self._buckets))
        bucket_chain: LinkedList = self._buckets[bucket_index]
        for (k, v) in bucket_chain:
            if k == key:
                return True
        return False

    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        raise NotImplementedError("HashMap.__iter__() is not implemented yet.")
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            return False
        if len(self) != len(other):
            return False
        current_self = self._buckets.head
        current_other = other._buckets.head
        while current_self and current_other:
            if current_self.data != current_other.data:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return True

    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
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