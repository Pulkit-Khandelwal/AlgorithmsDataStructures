class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.prev = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            print('empty stack!')
            return None

        to_pop = self.top
        self.top = self.top.prev

        print(to_pop.data)
        return to_pop.data

    def is_empty(self):
        if self.top is None:
            print('Boy! it is an empty stack. Push into it!')
            return True
        else:
            print('not empty!')
            return False

    def peek(self):
        print 'the current top element is'
        if self.top is None:
            print(self.top)
            return self.top
        else:
            print(self.top.data)
            return self.top.data


if __name__ == '__main__':

    from nose.tools import assert_equal

    print('Test: Empty stack')
    stack = Stack()
    assert_equal(stack.peek(), None)
    assert_equal(stack.pop(), None)

    print('Test: One element')
    top = Node(5)
    stack = Stack(top)
    assert_equal(stack.pop(), 5)
    assert_equal(stack.peek(), None)

    print('Test: More than one element')
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert_equal(stack.pop(), 3)
    assert_equal(stack.peek(), 2)
    assert_equal(stack.pop(), 2)
    assert_equal(stack.peek(), 1)
    assert_equal(stack.is_empty(), False)
    assert_equal(stack.pop(), 1)
    assert_equal(stack.peek(), None)
    assert_equal(stack.is_empty(), True)

    print('Success: test_end_to_end')
