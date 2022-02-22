from typing import Optional, Any


class Deque:
    """ Abstract Data Type Deque """

    def __init__(self):
        self.items: list = []

    def add_front(self, item: Any) -> None:
        self.items.insert(0, item)

    def add_rear(self, item: Any) -> None:
        self.items.append(item)

    def remove_front(self) -> Optional[Any]:
        if self.items:
            return self.items.pop(0)

    def remove_rear(self) -> Optional[Any]:
        if self.items:
            return self.items.pop()

    def peek_front(self) -> Optional[Any]:
        if self.items:
            return self.items[0]

    def peek_rear(self) -> Optional[Any]:
        if self.items:
            return self.items[-1]

    @property
    def size(self) -> int:
        return len(self.items)

    @property
    def is_empty(self) -> bool:
        return self.items == []
