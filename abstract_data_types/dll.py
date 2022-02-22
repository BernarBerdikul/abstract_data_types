from typing import Any, Optional


class DLLNode:
    """ Node for Doubly Linked list """
    def __init__(self, data):
        self.data: Any = data
        self.next: Optional[DLLNode] = None
        self.previous: Optional[DLLNode] = None

    def __repr__(self) -> str:
        return f"DLLNode object: {self.data}"

    def get_data(self) -> Any:
        return self.data

    def set_data(self, new_data: Any) -> None:
        self.data: Any = new_data

    def get_next(self) -> Any:
        return self.next

    def set_next(self, new_next: Any) -> None:
        self.next: Any = new_next

    def get_previous(self) -> Any:
        return self.previous

    def set_previous(self, new_previous: Any) -> None:
        self.previous: Any = new_previous


class DLL:
    """ Doubly Linked list """
    def __init__(self):
        self.head: Optional[DLLNode] = None

    def __repr__(self) -> str:
        return f"DLL object: {self.head}"

    def is_empty(self) -> bool:
        return self.head is None

    def add_front(self, new_data: Any) -> None:
        temp = DLLNode(data=new_data)
        temp.set_next(new_next=self.head)

        if self.head:
            self.head.set_previous(new_previous=temp)

        self.head: DLLNode = temp

    def size(self) -> int:
        """ O(n) """
        size: int = 0
        if self.head is None:
            return size
        current: DLLNode = self.head
        while current is not None:
            size += 1
            current = current.get_next()
        return size

    def search(self, data: Any) -> str or bool:
        if self.head is None:
            return "Linked List is empty"

        current: DLLNode = self.head
        while current is not None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False

    def remove(self, data: Any) -> Optional[str]:
        """ O(n) """
        if self.head is None:
            return "Linked List is empty. No Nodes to remove."

        current: DLLNode = self.head
        found: bool = False
        while not found:
            if current.get_data() == data:
                found: bool = True
            else:
                if current.get_next() is None:
                    return "A Node with that data value is not present."
                else:
                    current = current.get_next()
        if current.previous is None:
            self.head: DLLNode = current.get_next()
        else:
            current.previous.set_next(new_next=current.get_next())
            current.next.set_previous(new_previous=current.get_previous())
