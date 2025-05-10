from collections.abc import MutableSequence
from typing import Any, Protocol, TypeVar

class Comparable(Protocol):
    def __lt__(self, other: Any, /) -> bool: ...

T = TypeVar("T", bound=Comparable)

def insertion_sort(collection: MutableSequence[T]) -> MutableSequence[T]:
    for insert_index in range(1, len(collection)):
        insert_value = collection[insert_index]
        while insert_index > 0 and insert_value < collection[insert_index - 1]:
            collection[insert_index] = collection[insert_index - 1]
            insert_index -= 1
        collection[insert_index] = insert_value
    return collection
