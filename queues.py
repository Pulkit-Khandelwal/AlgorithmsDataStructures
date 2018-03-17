class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = next


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            self.tail = node

        return self.tail

    def dequeue(self):
        if self.head is None and self.tail is None:
            print('empty queueue')
            return None

        deq_item = self.head.data

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.next

        print(deq_item)

        return deq_item


if __name__ == '__main__':

    from nose.tools import assert_equal

    print('Test: Dequeue an empty queue')
    queue = Queue()
    assert_equal(queue.dequeue(), None)

    print('Test: Enqueue to an empty queue')
    queue.enqueue(1)

    print('Test: Dequeue a queue with one element')
    assert_equal(queue.dequeue(), 1)

    print('Test: Enqueue to a non-empty queue')
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print('Test: Dequeue a queue with more than one element')
    assert_equal(queue.dequeue(), 2)
    assert_equal(queue.dequeue(), 3)
    assert_equal(queue.dequeue(), 4)

    print('Success: test_end_to_end')

