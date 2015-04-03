# you must have mamba installed to run the test suite.
# execute the file with the mamba command.  E.g. mamba spec.py
from expects import *
import random

execfile('merge_sort.py')

with description('mergesort'):
    with context('when an empty list is provided'):
        with it('returns an empty list'):
            expect(mergesort([])).to(equal([]))
    with context('when a single element list is provided'):
        with it('returs the same single element list'):
            xs = [1]
            expect(mergesort(xs)).to(equal(xs))
    with context('when a two element list is provided'):
        with it('returns the same two element list sorted in ascending order'):
            xs = [3,1]
            expect(mergesort(xs)).to(equal(sorted(xs)))
    with context('when an unsorted list with 10 elements is provided'):
        with it('returns the sorted version of the list in ascending order'):
            xs = [7,5,9,10,234,32,21,8,0,1]
            expect(mergesort(xs)).to(equal(sorted(xs)))
    with context('when an unsorted list with over 1000 elements is provided'):
        with it('returns the sorted version of the list in ascending order'):
            xs = random.sample(xrange(100000), 2000)
            expect(mergesort(xs)).to(equal(sorted(xs)))
    with context('when there are duplicate elements'):
        with it('returns the sorted version of the list in ascending order'):
            xs = [2,8,7,8,0]
            expect(mergesort(xs)).to(equal(sorted(xs)))

