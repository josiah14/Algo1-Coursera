import itertools
import math

def karatsuba(x, y):
    # Python doesn't implement TCO, so use a loop instead
    return

def num_digits(n):
    return itertools.dropwhile(lambda exp: n / 10**exp > 0, itertools.count()).next()

def split(number, index):
    pow_ten = 10**index
    high_digits = number / pow_ten
    low_digits = number - high_digits*pow_ten
    return [high_digits, low_digits]

# This calculation is Monoidic and can easily be threaded with a little thought
class BinaryRecursionTree:
    def __init__(self, datum, counter, mapper, reducer):
        self._datum = datum
        self._datum_size = counter(max(datum))
        self._base_nodes = []
        self._base_nodes_count = None
        self._last_full_level_size = None
        self._height = None
        self._tree = mapper(self._datum, self._datum_size / 2)
        self._tree.append(self._datum_size / 2)
        self._mapper = mapper
        self._reducer = reducer
        self._counter = counter

    class ref:
        def __init__(self, obj): self.obj = obj
        def get(self):           return self.obj

    def _get_tree_node(self, path):
        tree = self._tree
        for i in path:
            tree = tree[i]
        return tree

    def _build_tree(self):
        nodes = [self.ref(self._tree)]
        nodes0 = []
        for i in range(0, self.height() - 1):
            for j in range(0, 2**i):
                for leaf in range(0,2):
                    num = nodes[j].get()[leaf]
                    nodes[j].get()[leaf] = self._mapper(num, self._counter(num) / 2)
                    half_num_digits = self._counter(max(nodes[j].get()[leaf])) / 2
                    nodes[j].get()[leaf].append(half_num_digits)
                    nodes0.append(self.ref(nodes[j].get()[leaf]))
            nodes = nodes0
            nodes0 = []
        for base_node in self._base_nodes:
            node = self._get_tree_node(base_node[:-1])
            node[base_node[-1]] = self._mapper(node[base_node[-1]], 1)
            node[base_node[-1]].append(0)

    def build(self):
        for index in range(0, self.base_nodes_count()):
            self._base_nodes.append([int(char) for char in bin(index)[:1:-1]])
            while len(self._base_nodes[index]) < self.height(): self._base_nodes[index].append(0)
        self._build_tree()

    def base_nodes_count(self):
        if self._base_nodes_count == None: self._base_nodes_count = self._datum_size - self.last_full_level_size()
        return self._base_nodes_count

    def last_full_level_size(self):
        self._last_full_level_size = self._last_full_level_size or int(2**(self.height()))
        return self._last_full_level_size

    def height(self):
        self._height = self._height or int(math.ceil(math.log(self._datum_size, 2)) - 1)
        return self._height

