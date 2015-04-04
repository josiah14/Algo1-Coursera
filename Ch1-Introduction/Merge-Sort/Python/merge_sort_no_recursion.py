def mergesort(xs):
    if len(xs) < 2:
        return xs
    ys = _divide(xs)
    while len(ys) > 1:
      yInit, yTail = split_at(ys, 2)
      ys = yTail + [_conquer(yInit[0], yInit[1])]
    return ys[0]

def _divide(xs):
    return [ [y] for y in xs ]

# not thread safe
def _conquer(left_xs, right_xs):
    # copy the lists to avoid side-effects
    left = list(left_xs)
    right = list(right_xs)

    sorted_xs = []
    while left and right:
        left0 = head(left)
        right0 = head(right)
        if left0 < right0:
            sorted_xs.append(left0)
            left = tail(left)
        else:
            sorted_xs.append(right0)
            right = tail(right)
    return sorted_xs + right + left

# helper methods that could probably be pulled into a library
def split_at(xs, index):
    return (xs[:index], xs[index:])

def tail(xs):
    return xs[1:]

def head(xs):
    return xs[0]

