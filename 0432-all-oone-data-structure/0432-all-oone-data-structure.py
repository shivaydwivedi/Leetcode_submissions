class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:

    def __init__(self):
        self.keyMap = {}  # key -> Node

        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.keyMap:
            if self.head.next.count != 1:
                new_node = Node(1)
                self._add_node_after(new_node, self.head)
            self.head.next.keys.add(key)
            self.keyMap[key] = self.head.next
        else:
            curr = self.keyMap[key]
            next_count = curr.count + 1

            if curr.next.count != next_count:
                new_node = Node(next_count)
                self._add_node_after(new_node, curr)
            curr.next.keys.add(key)
            self.keyMap[key] = curr.next

            curr.keys.remove(key)
            if not curr.keys:
                self._remove_node(curr)

    def dec(self, key: str) -> None:
        curr = self.keyMap[key]

        if curr.count == 1:
            del self.keyMap[key]
        else:
            prev_count = curr.count - 1

            if curr.prev.count != prev_count:
                new_node = Node(prev_count)
                self._add_node_after(new_node, curr.prev)
            curr.prev.keys.add(key)
            self.keyMap[key] = curr.prev

        curr.keys.remove(key)
        if not curr.keys:
            self._remove_node(curr)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()