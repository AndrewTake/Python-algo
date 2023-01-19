import random
from solution import merge_sort_bottom_up
from common_test_cases import AntiDiscoveryWrapper


class MergeSortTest(AntiDiscoveryWrapper.CommonTestCase):
    def setUp(self):
        self._function_under_test = merge_sort_bottom_up

    def test_empty(self):
        self.do_test([])

    def test_mergesort_sixteen(self):
        self.do_test(random.sample(range(99), 16))

    def test_mergesort_eight(self):
        self.do_test(random.sample(range(99), 8))

    def test_mergesort_31(self):
        self.do_test(random.sample(range(99), 31))
