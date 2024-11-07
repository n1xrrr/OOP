class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None

    def __len__(self):
        count = 0
        current = self.start
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.start
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def append(self, obj):
        new_node = Node(obj)
        if self.start is None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def remove(self, index):
        if index == 0:
            if self.start:
                self.start = self.start.next
        else:
            current = self.start
            for i in range(index - 1):
                if current is None:
                    return
                current = current.next
            if current is None or current.next is None:
                return
            current.next = current.next.next