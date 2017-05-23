import unittest
SEEK_NODE_INDEX = 0
PREV_NODE_INDEX = 1

class SimpleLinkedList():
    # simple implementation of linked list.
    # internal data structure only contains a start node which is hidden.
    # nodes object will not be exposed to the user as it is an implementation detail.
    def __init__(self):
        self._start_node = None

    def insert(self, position, data):
        #insert a new node with data at position
        if position == 0:
            self._start_node = Node(data=data, ptr=self._start_node)
        else:
            seeked_node, _ = self._seek_to_position(position)
            new_node = Node(data=data, ptr=seeked_node.ptr)
            seeked_node.ptr = new_node

    def __iter__(self):
        #overwrites the iter method as a generator to allow casting to list
        self.__internal_cursor = self._start_node
        yield self.__internal_cursor.data
        try:
            while True:
                self.__internal_cursor = self.__internal_cursor.next()
                yield self.__internal_cursor.data
        except StopIteration:
            pass

    def duplicate(self):
        #makes a copy (used for testing purposes)
        list_of_items = list(self)
        new_linked_list = SimpleLinkedList()
        for i in list_of_items:
            new_linked_list.add(i)
        return new_linked_list

    def add(self, data):
        #append a node with data at the end
        if self._start_node:
            last_node, _ = self._goto_last_node()
            new_node = Node(data=data, ptr=None)
            last_node.ptr = new_node

        else:
            self._start_node = Node(data=data, ptr=None)

    def delete(self, index):
        #delete a note at index
        if index == 0:
            self._start_node, _ = self._seek_to_position(index + 1)
        else:
            seeked_node, previous_node = self._seek_to_position(index)
            previous_node.ptr = seeked_node.ptr

    def pop(self):
        #removes node at the last index
        current_node, previous_node = self._goto_last_node()
        temp_current_node_data = current_node.data
        previous_node.ptr = None
        return temp_current_node_data

    def __getitem__(self, index):
        #magic method to access index through [index]
        return self.get(index)

    def __setitem__(self, index, value):
        #magic method to set value at index
        self._seek_to_position(index)[SEEK_NODE_INDEX].data = value

    def get(self, index):
        #get method to get the value at index
        return self._seek_to_position(index)[SEEK_NODE_INDEX].data

    def _seek_to_position(self, position):
        # move along the linked list and return the seeked node and the node before the seeked node
        seeked_node = self._start_node
        previous_node = None

        for placement in range(position):
            previous_node = seeked_node
            seeked_node = seeked_node.next()
            if seeked_node is None:
                raise ValueError(f'the linked list does not have index beyond {position}')

        return seeked_node, previous_node

    def _goto_last_node(self):
        # used for pop and add
        last_node = self._start_node
        while True:
            try:
                previous_node = last_node
                last_node = last_node.next()

            except StopIteration:
                return last_node, previous_node


class Node():
    # datastructure that contains data and a ptr which is the reference to the next node, if ptr is None, the node is terminal node
    def __init__(self, data, ptr):
        self.data = data
        self.ptr = ptr

    def next(self):
        if self.ptr is None:
            raise StopIteration
        return self.ptr


class LinkedListTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.linked_list = SimpleLinkedList()
        for n in range(10):
            cls.linked_list.add(n)

    def test_add_method(self):
        linked_list = SimpleLinkedList()
        linked_list.add(1)
        self.assertEqual(linked_list._start_node.data, 1)
        self.assertEqual(linked_list._start_node.ptr, None)

    def test_iteration(self):
        to_list = list(self.linked_list)
        self.assertEqual(len(to_list), 10)
        for index, item in enumerate(to_list):
            self.assertEqual(type(item), int)
            self.assertEqual(item, index)


    def test_insert_beginning(self):
        new_list = self.linked_list.duplicate()
        new_list.insert(0, -1)
        self.assertEqual(len(list(new_list)), 11)
        self.assertEqual(list(new_list)[0], -1)
        for n in range(10):
            self.assertEqual(list(new_list)[n + 1], n)

    def test_insert_middle(self):
        new_list = self.linked_list.duplicate()
        new_list.insert(5, -1)
        self.assertEqual(len(list(new_list)), 11)
        self.assertEqual(list(new_list)[6], -1)
        for n in range(5):
            self.assertEqual(list(new_list)[n], n)
        for n in range(7, 10):
            self.assertEqual(list(new_list)[n], n - 1)

    def test_insert_last(self):
        new_list = self.linked_list.duplicate()
        new_list.insert(9, -1)
        self.assertEqual(len(list(new_list)), 11)
        self.assertEqual(list(new_list)[10], -1)
        for n in range(10):
            self.assertEqual(list(new_list)[n], n)

    def test_delete_beginning(self):
        new_list = self.linked_list.duplicate()
        new_list.delete(0)
        self.assertEqual(len(list(new_list)), 9)
        for n in range(9):
            self.assertEqual(list(new_list)[n], n + 1)

    def test_delete_middle(self):
        new_list = self.linked_list.duplicate()
        new_list.delete(5)
        self.assertEqual(len(list(new_list)), 9)
        for n in range(5):
            self.assertEqual(list(new_list)[n], n)
        for n in range(5, 9):
            self.assertEqual(list(new_list)[n], n + 1)

    def test_delete_last(self):
        new_list = self.linked_list.duplicate()
        new_list.delete(9)
        self.assertEqual(len(list(new_list)), 9)
        for n in range(9):
            self.assertEqual(list(new_list)[n], n)
    def test_getitem(self):
        new_list = self.linked_list.duplicate()
        self.assertTrue(all(
            new_list[n] == new_list.get(n)
            for n in range(10)))

    def test_setitem(self):
        new_list = self.linked_list.duplicate()
        for n in range(10):
            new_list[n] = 'a'
        self.assertTrue(all(
            new_list[n] == 'a'
            for n in range(10)))
