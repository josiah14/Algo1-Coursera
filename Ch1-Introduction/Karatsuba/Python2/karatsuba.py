import itertools

def karatsuba(x, y):
    # Python doesn't implement TCO, so use a loop instead
    return

def num_digits(n):
    return itertools.dropwhile(lambda exp: n / 10**exp > 0, itertools.count()).next()

def split(n, m):
    pow_ten = 10**m
    high_digits = n / pow_ten
    low_digits = n - high_digits*pow_ten
    return high_digits, low_digits

# This calculation is Monoidic and can easily be threaded with a little thought
class SplitTree(n, m):
    def __init__(self, number, digit_count):
        self._number = number
        self._digit_count = digit_count
        self._base_leaf_locations = []

    def build(self):
        for index in range(0, self.base_nodes_count()):
            self._base_leaf_locations.append([int(char) for char in bin(index)[:1:-1]])
            while len(self._base_leaf_locations) < self.height(): self._base_leaf_locations[index].append(0)
        # the rest of the leaves can be found by continuing to iterate through the range(index, self.base_nodes_count())
        # with self.height() - 1 list sizes

    def base_nodes_count(self):
        if self._base_nodes_count == None: self._base_nodes_count = self._digit_count - self.last_full_level_size()
        return self._base_nodes_count

    def last_full_level_size(self):
        self._last_full_level_size = self._last_full_level_size or 2**(self.height())
        return self._last_full_level_size

    def height(self):
        self._height = self._height or math.ceil(math.log(self._digit_count, 2)) - 1
        return self._height

