from itertools import *
from math import *

def karatsuba(x, y):
    tree = TrinaryRecursionTree([x,y],
                                num_digits,
                                split_multiple,
                                split_formula,
                                base_formula
                               )
    tree.build()
    tree.aggregate()
    return tree._tree

def base_formula(z0, z1, z2, m):
    return z2 * (10**(2*m)) + (z1 - z2 - z0) * (10**m) + z0

def split_formula(x1, xs, x0, y1, ys, y0, m):
    return base_formula(x0 * y0, xs * ys, x1 * y1, m)

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
class TrinaryRecursionTree:
    def __init__(self, datum, counter, mapper, reducer, recursor):
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
        self._recursor = recursor
        self._counter = counter
        self._nodes = [self.ref(self._tree)]

    class ref:
        def __init__(self, obj): self.obj = obj
        def get(self):           return self.obj

    def _flatten2(self, two_d_iterable):
        print two_d_iterable
        return [item for subiter in two_d_iterable for item in subiter]

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
        print "build_tree"
        for i in range(0, self.height() - 1):
            print "tree"
            print self._tree
            max_val = max(self._flatten2(
                imap(lambda node: [node.get()[0],node.get()[2],node.get()[3],node.get()[5]], self._nodes)
            ))
            print "max"
            print max_val
            split_index = self._counter( max_val ) / 2
            print "index"
            print split_index
            for j in range(0, 3**i):
                x1 = self._nodes[j].get().pop(0)
                xs = self._nodes[j].get().pop(0)
                x0 = self._nodes[j].get().pop(0)
                y1 = self._nodes[j].get().pop(0)
                ys = self._nodes[j].get().pop(0)
                y0 = self._nodes[j].get().pop(0)
                self._nodes[j].get().insert(0, self._mapper(split_index, x1, y1))
                self._nodes[j].get().insert(1, self._mapper(split_index, xs, ys))
                self._nodes[j].get().insert(2, self._mapper(split_index, x0, y0))
                self._nodes[j].get()[0].append(split_index)
                self._nodes[j].get()[1].append(split_index)
                self._nodes[j].get()[2].append(split_index)
                nodes0.append(self.ref(self._nodes[j].get()[0]))
                nodes0.append(self.ref(self._nodes[j].get()[1]))
                nodes0.append(self.ref(self._nodes[j].get()[2]))
            self._nodes = nodes0
            nodes0 = []
        base_nodes = self._base_nodes
        if 3**self.height() / 2 < len(self._base_nodes):
            base_nodes = base_nodes[:(3**self.height() / 2)]
        for base_node in base_nodes:
            print self._tree
            node = self._get_tree_node(base_node)
            print node
            split_index = self._counter(max(node)) / 2
            x1 = node.pop(0)
            xs = node.pop(0)
            x0 = node.pop(0)
            y1 = node.pop(0)
            ys = node.pop(0)
            y0 = node.pop(0)
            node.insert(0, self._mapper(split_index, x1, y1))
            node.insert(1, self._mapper(split_index, xs, ys))
            node.insert(2, self._mapper(split_index, x0, y0))
            node[0].append(0)
            node[1].append(0)
            node[2].append(0)
            nodes0.append(self.ref(node[0]))
            nodes0.append(self.ref(node[1]))
            nodes0.append(self.ref(node[2]))
        self._nodes = nodes0
        nodes0 = []
        print self._tree

    def build(self):
        for index in range(0, self.base_nodes_count()):
            self._base_nodes.append([int(char) for char in self._trin(index)[::-1]])
            while len(self._base_nodes[index]) < self.height(): self._base_nodes[index].append(0)
        self._build_tree()

    def aggregate(self):
        for i in range(0,self.base_nodes_count()):
            cur_base_node = self._base_nodes[i]
            for j in range(0,3):
                print j
                print self._get_tree_node(cur_base_node)
                self._get_tree_node(cur_base_node)[j] = self._reducer(*self._nodes[i*3 + j].get())
            cur_node = self._get_tree_node(cur_base_node[:-1])
            cur_node[cur_base_node[-1]] = self._recursor(*cur_node[cur_base_node[-1]])
        remaining_bottom_leaves = range(self.base_nodes_count(), 3**(self.height() - 1))
        bottom_leaf_paths = [[int(char) for char in self._trin(leaf)[::-1]] for leaf in remaining_bottom_leaves]
        for index in range(0, len(bottom_leaf_paths)):
            while len(bottom_leaf_paths[index]) < self.height() - 1: bottom_leaf_paths[index].append(0)
        for leaf_path in bottom_leaf_paths:
            node = self._get_tree_node(leaf_path[:-1])
            node[leaf_path[-1]] = self._reducer(*node[leaf_path[-1]])
        new_height = self.height() - 2
        while new_height > 0:
            print new_height
            bottom_leaf_paths = [[int(char) for char in self._trin(leaf)[::-1]] for leaf in range(0, 3**new_height)]
            for index in range(0, len(bottom_leaf_paths)):
                while len(bottom_leaf_paths[index]) < new_height: bottom_leaf_paths[index].append(0)
            print bottom_leaf_paths
            for leaf_path in bottom_leaf_paths:
                node = self._get_tree_node(leaf_path[:-1])
                print node
                node[leaf_path[-1]] = self._recursor(*node[leaf_path[-1]])
                print node
            new_height -= 1
        x._tree = x._recursor(*x._tree)

    def base_nodes_count(self):
        if self._base_nodes_count == None: self._base_nodes_count = self._datum_size - 3**self.last_full_level_size()
        return self._base_nodes_count

    def last_full_level_size(self):
        self._last_full_level_size = self._last_full_level_size or int(3**(self.height() - 1))
        return self._last_full_level_size

    def height(self):
        self._height = self._height or int(ceil(log(self._datum_size, 2)))
        return self._height

