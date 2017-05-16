class TestIter2():

    def __iter__(self):
        # self.counter = 0
        return self

    def __next__(self):
        # self.counter += 1
        # if self.counter <= 10:
        yield 1
        raise StopIteration


b = TestIter2()
for i in b:
    print(i)
    for t in i:
        print(t)


class TestIter():

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        self.counter += 1
        if self.counter <= 10:
            return self.some_gen(self.counter)
        raise StopIteration

    def some_gen(self,numb):
        for n in range(numb):
            yield n
a = TestIter()
list_of_gens = (i for i in a)
blah = [ [i for i in gen] for gen in list_of_gens]