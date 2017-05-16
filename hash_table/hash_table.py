import unittest

class KeyValuePair:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __hash__(self):
        return object.__hash__(self.key)


class SimpleHashTable:
    #simple hashtable. allows the lookup of the key/value pair in O(1) time
    #uses a list to store the data in the bin
    def __init__(self):
        self._bins = {}


    def __hash_func(self,key):
        #calculate the hash number based on the key
        return hash(key)

    def __key_to_bin(self, key):
        #maps hash number into bin number
        return self.__hash_func(key) % len(key)

    def insert(self, key,value):
        #insert the key and its corresponding value into the hashmap
        #1.given the key, map it to integer,
        #2.use the hash funciton to place it in bin
        #2b. create a list, or linked list if bin is empty
        #3.if key is duplicated in bin, replace the value
        bin_num =  self.__key_to_bin(key)
        if not bin_num in self._bins:
            self._bins[bin_num] = []
        for item in self._bins[bin_num]:
            if item.key is key:
                item.value = value
                return
        self._bins[bin_num].append(KeyValuePair(key,value))


    def lookup(self,key):
        #look up the value in the hashmap
        bin_num = self.__key_to_bin(key)
        for item in self._bins[bin_num]:
            if item.key is key:
                return item.value
        raise KeyError(f'{key} does not exist')

    def delete(self,key):
        #remove the key and the value associated with that key
        bin_num = self.__key_to_bin(key)
        for item in self._bins[bin_num]:
            if item.key is key:
                self._bins[bin_num].remove(item)
                return
        raise KeyError(f'{key} does not exist, cannot remove')




class TestSimpleHashTable(unittest.TestCase):


    def test_insert(self):
        #test the insert operation
        hash_table = SimpleHashTable()
        hash_table.insert('a',1)


    def test_lookup(self):
        #test the lookup functionality of the hashtable
        hash_table = SimpleHashTable()
        hash_table.insert('a',2)
        self.assertEqual(hash_table.lookup('a'),2)

        pass

    def test_remove(self):
        #test the removal of the hashtable
        hash_table = SimpleHashTable()
        hash_table.insert('a',2)
        hash_table.insert('b',3)
        hash_table.delete('b')
        with self.assertRaises(KeyError):
            hash_table.lookup('b')
