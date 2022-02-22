from typing import Any, Optional


class Stack:
    """ Abstract Data Type Stack """

    def __init__(self):
        self.items: list = []

    def push(self, item: Any) -> None:
        """
        Accepts an item as a parameter and appends it to
        the end of the list.

        The runtime for this method is O(1) or constant time
        :param item: Any
        :return: None
        """
        self.items.append(item)

    def pop(self) -> Optional[Any]:
        """
        Removes and returns the last item for the list,
        which is also the top item of the Stack

        The runtime here is constant time
        :return: the last item from list
        """
        if self.items:
            return self.items.pop()

    def peek(self) -> Optional[Any]:
        """
        Returns the last item for the list,
        which is also the top item of the Stack

        The runtime here is constant time
        :return: the last item from list
        """
        if self.items:
            return self.items[-1]

    def size(self) -> int:
        """
        Return the length of the stack
        The runtime here is constant time
        :return: int, count of elements in Stack
        """
        return len(self.items)

    def is_empty(self) -> bool:
        """
        The runtime here is constant time
        :return: bool, True if Stack is empty
        """
        return self.items == []
