from itertools import *
from math import *

def karatsuba(x, y):
    # Python doesn't implement TCO, so use a loop instead
    return

def formula(x0, x1, y0, y1, m):
    z0 = x0 * y0
    z1 = (x0 + x1) * (y0 + y1)
    z2 = x1 * y1
    return z2 * (10**(2*m)) + (z1 - z2 - z0) * (10**m) + z0

def num_digits(n):
    return dropwhile(lambda exp: n / 10**exp > 0, count()).next()

def split(number, index):
    pow_ten = 10**index
    high_digits = number / pow_ten
    low_digits = number - high_digits*pow_ten
    sum_digits = high_digits + low_digits
    return [high_digits, sum_digits, low_digits]

def split_multiple(index, *numbers):
    return reduce(lambda x, y: x + y, [split(num, index) for num in numbers])

# This calculation is Monoidic and can easily be threaded with a little thought
class BinaryRecursionTree:
    def __init__(self, datum, counter, mapper, reducer):
        self._datum = datum
        self._datum_size = counter(max(datum))
        self._base_nodes = []
        self._base_nodes_count = None
        self._last_full_level_size = None
        self._height = None
        self._tree = mapper(self._datum_size / 2, *self._datum)
        self._tree.append(self._datum_size / 2)
        self._mapper = mapper
        self._reducer = reducer
        self._counter = counter
        self._nodes = [self.ref(self._tree)]

    class ref:
        def __init__(self, obj): self.obj = obj
        def get(self):           return self.obj

    def _flatten2(self, two_d_iterable): return [item for subiter in two_d_iterable for item in subiter]

    def _trin(self, base_10_num):
        base_3_num_str = ''
        while base_10_num:
            base_3_num_str = str(base_10_num%3) + base_3_num_str
            base_10_num = base_10_num / 3
        return base_3_num_str

    def _get_tree_node(self, path):
        tree = self._tree
        for i in path:
            tree = tree[i]
        return tree

    def _build_tree(self):
        nodes0 = []
        for i in range(0, self.height() - 1):
            print self._tree
            split_index = self._counter( max(self._flatten2(imap(lambda node: node.get(), self._nodes))) ) / 2
            for j in range(0, 3**i):
                x0 = self._nodes[j].get().pop(0)
                xs = self._nodes[j].get().pop(0)
                x1 = self._nodes[j].get().pop(0)
                y0 = self._nodes[j].get().pop(0)
                ys = self._nodes[j].get().pop(0)
                y1 = self._nodes[j].get().pop(0)
                self._nodes[j].get().insert(0, self._mapper(split_index, x1, y1))
                self._nodes[j].get().insert(0, self._mapper(split_index, xs, ys))
                self._nodes[j].get().insert(0, self._mapper(split_index, x0, y0))
                self._nodes[j].get()[0].append(split_index)
                self._nodes[j].get()[1].append(split_index)
                self._nodes[j].get()[2].append(split_index)
                nodes0.append(ref(self._nodes[j].get()[0]))
                nodes0.append(ref(self._nodes[j].get()[1]))
                nodes0.append(ref(self._nodes[j].get()[2]))
            self._nodes = nodes0
            nodes0 = []
        base_nodes = self._base_nodes
        if 3**self.height() / 2 < len(self._base_nodes):
            base_nodes = base_nodes[:(3**self.height() / 2)]
        for base_node in base_nodes:
            print self._tree
            node = self._get_tree_node(base_node[:-1])
            split_index = self._counter(max(node)) / 2
            x0 = node.pop(0)
            xs = node.pop(0)
            x1 = node.pop(0)
            y0 = node.pop(0)
            ys = node.pop(0)
            y1 = node.pop(0)
            node.insert(0, self._mapper(split_index, x1, y1))
            node.insert(0, self._mapper(split_index, xs, ys))
            node.insert(0, self._mapper(split_index, x0, y0))
            node[0].append(0)
            node[1].append(0)
            node[2].append(0)
            nodes0.append(ref(node[0]))
            nodes0.append(ref(node[1]))
            nodes0.append(ref(node[2]))
        self._nodes = nodes0
        nodes0 = []
        print self._tree

    def build(self):
        for index in range(0, self.base_nodes_count()):
            self._base_nodes.append([int(char) for char in self._trin(index)[::-1]]) # need some way to use base 3 here.
            while len(self._base_nodes[index]) < self.height(): self._base_nodes[index].append(0)
        self._build_tree()

    def base_nodes_count(self):
        if self._base_nodes_count == None: self._base_nodes_count = self._datum_size - self.last_full_level_size() / 3
        return self._base_nodes_count

    def last_full_level_size(self):
        self._last_full_level_size = self._last_full_level_size or int(3**(self.height()))
        return self._last_full_level_size

    def height(self):
        self._height = self._height or int(ceil(log(self._datum_size, 2)) - 1)
        return self._height

