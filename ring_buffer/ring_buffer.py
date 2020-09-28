class ListNode:
    def __init__(self, value, prev_node=None, next_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node
            
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
            
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.tail is None: 
            self.head = new_node
            self.tail = new_node
            self.length +=1
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, new_value):
        if self.current is None:
            self.storage.add_to_tail(new_value)
            self.current = self.storage.head
            return
        if len(self.storage) >= self.capacity:
            if self.current != self.storage.tail:
                self.current.next.value = new_value
                self.current = self.current.next
            else:
                self.current = self.storage.head
                self.current.value = new_value
        else:
            self.storage.add_to_tail(new_value)
            self.current = self.current.next
                

    def get(self):
        ring_values = []
        current = self.storage.head
        while current:
            ring_values.append(current.value)
            current = current.next

        return ring_values