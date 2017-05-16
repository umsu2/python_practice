import unittest


class SimpleinkedList():
    def __init__(self):
        self._start_node = None

    def insert(self, position, data):
        if position == 0:
            self._start_node = Node(data=data, ptr=self._start_node)
        else:
            seeked_node, _ = self._seek_to_position(position)
            new_node = Node(data=data, ptr=seeked_node.ptr)
            seeked_node.ptr = new_node

    def __iter__(self):
        self.__internal_cursor = self._start_node
        yield self.__internal_cursor
        try:
            while True:
                self.__internal_cursor = self.__internal_cursor.next()
                yield self.__internal_cursor
        except StopIteration:
            pass

    def duplicate(self):
        list_of_items = list(self)
        new_linked_list = SimpleinkedList()
        for i in list_of_items:
            new_linked_list.add(i.data)
        return new_linked_list

    def add(self, data):
        if self._start_node:
            last_node, _ = self._goto_last_node()
            new_node = Node(data=data, ptr=None)
            last_node.ptr = new_node

        else:
            self._start_node = Node(data=data, ptr=None)

    def delete(self, position):
        if position == 0:
            self._start_node, _ = self._seek_to_position(position + 1)
        else:
            seeked_node, previous_node = self._seek_to_position(position)
            previous_node.ptr = seeked_node.ptr

    def pop(self):
        _, previous_node = self._goto_last_node()
        previous_node.ptr = None

    def get(self, index):
        return self._seek_to_position(index)

    def _seek_to_position(self, position):

        seeked_node = self._start_node
        previous_node = None

        for placement in range(position):
            previous_node = seeked_node
            seeked_node = seeked_node.next()
            if seeked_node is None:
                raise ValueError(f'the linked list does not have index beyond {position}')

        return seeked_node, previous_node

    def _goto_last_node(self):
        last_node = self._start_node
        while True:
            try:
                previous_node = last_node
                last_node = last_node.next()

            except StopIteration:
                return last_node, previous_node


class Node():
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
        cls.linked_list = SimpleinkedList()
        for n in range(10):
            cls.linked_list.add(n)

    def test_add_method(self):
        linked_list = SimpleinkedList()
        linked_list.add(1)
        self.assertEqual(linked_list._start_node.data, 1)
        self.assertEqual(linked_list._start_node.ptr, None)

    def test_iteration(self):
        to_list = list(self.linked_list)
        self.assertEqual(len(to_list), 10)
        for index, item in enumerate(to_list):
            self.assertEqual(type(item), Node)
            self.assertEqual(item.data, index)

    def test_duplicate(self):
        linked_list1 = list(self.linked_list.duplicate())
        for index, item in enumerate(self.linked_list):
            self.assertEqual(item.data, linked_list1[index].data)
            self.assertNotEqual(item, linked_list1[index])

    def test_insert_beginning(self):
        new_list = self.linked_list.duplicate()
        new_list.insert(0, -1)
        self.assertEqual(len(list(new_list)), 11)
        self.assertEqual(list(new_list)[0].data, -1)
        for n in range(10):
            self.assertEqual(list(new_list)[n + 1].data, n)

    def test_insert_middle(self):
        new_list = self.linked_list.duplicate()
        new_list.insert(5, -1)
        self.assertEqual(len(list(new_list)), 11)
        self.assertEqual(list(new_list)[6].data, -1)
        for n in range(5):
            self.assertEqual(list(new_list)[n].data, n)
        for n in range(7, 10):
            self.assertEqual(list(new_list)[n].data, n - 1)

    def test_insert_last(self):
        new_list = self.linked_list.duplicate()
        new_list.insert(9, -1)
        self.assertEqual(len(list(new_list)), 11)
        self.assertEqual(list(new_list)[10].data, -1)
        for n in range(10):
            self.assertEqual(list(new_list)[n].data, n)

    def test_delete_beginning(self):
        new_list = self.linked_list.duplicate()
        new_list.delete(0)
        self.assertEqual(len(list(new_list)), 9)
        for n in range(9):
            self.assertEqual(list(new_list)[n].data, n + 1)

    def test_delete_middle(self):
        new_list = self.linked_list.duplicate()
        new_list.delete(5)
        self.assertEqual(len(list(new_list)), 9)
        for n in range(5):
            self.assertEqual(list(new_list)[n].data, n)
        for n in range(5, 9):
            self.assertEqual(list(new_list)[n].data, n + 1)

    def test_delete_last(self):
        new_list = self.linked_list.duplicate()
        new_list.delete(9)
        self.assertEqual(len(list(new_list)), 9)
        for n in range(9):
            self.assertEqual(list(new_list)[n].data, n)
