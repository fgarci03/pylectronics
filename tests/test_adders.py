from unittest import TestCase

from src.adders import HalfAdder, FullAdder, FourBitFullAdder
from tests.utils import decimal_to_boolean_list


class HalfAdderTests(TestCase):

    TRUTH_TABLE = (
        # A      B        S      Cout
        ((False, False), (False, False)),
        ((False, True), (True, False)),
        ((True, False), (True, False)),
        ((True, True), (False, True)),
    )

    def setUp(self):
        self.half_adder = HalfAdder()

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            assert self.half_adder.set_inputs(*test_case[0]) == test_case[1]


class FullAdderTests(TestCase):

    TRUTH_TABLE = (
        # A      B      Cin      S      Cout
        ((False, False, False), (False, False)),
        ((False, False, True), (True, False)),
        ((False, True, False), (True, False)),
        ((False, True, True), (False, True)),
        ((True, False, False), (True, False)),
        ((True, False, True), (False, True)),
        ((True, True, False), (False, True)),
        ((True, True, True), (True, True)),
    )

    def setUp(self):
        self.full_adder = FullAdder()

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            assert self.full_adder.set_inputs(*test_case[0]) == test_case[1]


class FourBitFullAdderTests(TestCase):
    def setUp(self):
        self.full_adder = FourBitFullAdder()
        self.TRUTH_TABLE = []

        # Generate the truth table, since it is HUGE for a 4 bit adder
        # Note: it will generate items like:
        #    (((False, True, False, False), (False, False, True, True)), (False, False, True, True, True))
        #    and
        #    (((False, True, True, False), (False, True, True, True)), (False, True, True, False, True))
        # for 4 + 3 = 7 and 6 + 7 = 13, respectively
        for addend_1 in range(0, 16):
            for addend_2 in range(0, 16):
                self.TRUTH_TABLE.append(
                    (
                        (decimal_to_boolean_list(addend_1, padding=4), decimal_to_boolean_list(addend_2, padding=4)),
                        decimal_to_boolean_list(addend_1 + addend_2, padding=5),
                    )
                )

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            # Note, generate the inputs arguments by setting both addends and the carry in (which is always 0 *false*)
            inputs = (test_case[0][0], test_case[0][1], False)
            assert self.full_adder.set_inputs(*inputs) == test_case[1]

        # Test adding 15+15 with a carry in, which will result in 31
        assert (
            self.full_adder.set_inputs(
                value_1=(True, True, True, True),
                value_2=(True, True, True, True),
                carry_in=True,
            )
            == (True, True, True, True, True)
        )
