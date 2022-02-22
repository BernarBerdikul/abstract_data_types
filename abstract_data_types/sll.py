from typing import Any, Optional


class SLLNode:
    """ Node for Singly Linked list """
    def __init__(self, data):
        self.data: Any = data
        self.next: Optional[SLLNode] = None

    def __repr__(self) -> str:
        return f"SLLNode object: {self.data}"

    def get_data(self) -> Any:
        return self.data

    def set_data(self, new_data: Any) -> None:
        self.data: Any = new_data

    def get_next(self) -> Any:
        return self.next

    def set_next(self, new_next: Any) -> None:
        self.next: Any = new_next


class SLL:
    """ Singly Linked list """
    def __init__(self):
        self.head: Optional[SLLNode] = None

    def __repr__(self) -> str:
        return f"SLL object: {self.head}"

    def is_empty(self) -> bool:
        return self.head is None

    def add_front(self, new_data: Any) -> None:
        temp = SLLNode(data=new_data)
        temp.set_next(new_next=self.head)
        self.head: SLLNode = temp

    def size(self) -> int:
        size: int = 0
        if self.head is None:
            return size
        current: SLLNode = self.head
        while current is not None:
            size += 1
            current = current.get_next()
        return size

    def search(self, data: Any) -> str or bool:
        if self.head is None:
            return "Linked List is empty"

        current: SLLNode = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False

    def remove(self, data: Any) -> Optional[str]:
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current: SLLNode = self.head
        previous: Optional[SLLNode] = None
        found: bool = False
        while not found:
            if current.get_data() == data:
                found: bool = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present."
                else:
                    previous = current
                    current = current.get_next()
        if previous is None:
            self.head: SLLNode = current.get_next()
        else:
            previous.set_next(new_next=current.get_next())
